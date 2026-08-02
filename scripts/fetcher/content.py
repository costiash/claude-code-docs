"""
Content fetching and validation functionality.

This module handles:
- Fetching markdown content from documentation URLs
- Validating markdown content
- Saving markdown files
- Fetching the Claude Code changelog
"""

import hashlib
import random
import re
import time
from pathlib import Path
from typing import Tuple, Union

import requests

from .config import (
    HEADERS,
    MAX_RETRIES,
    RETRY_DELAY,
    MAX_RETRY_DELAY,
    logger,
)

# Retry-After handling: default when the header is absent/unparseable, and a hard
# cap so a hostile/buggy header can never stall the pipeline for hours.
DEFAULT_RETRY_AFTER = 60
MAX_RETRY_AFTER = 300


def _retry_after_seconds(response) -> int:
    """
    Parse a 429 response's Retry-After header defensively.

    HTTP allows either delta-seconds or an HTTP-date; a bare ``int()`` raises
    ValueError on the date form (killing the page for the run via the wrong
    handler). Unparseable/absent values fall back to ``DEFAULT_RETRY_AFTER``;
    the result is clamped to ``[0, MAX_RETRY_AFTER]``.
    """
    raw = response.headers.get('Retry-After', DEFAULT_RETRY_AFTER)
    try:
        seconds = int(raw)
    except (TypeError, ValueError):
        logger.warning(f"Unparseable Retry-After header {raw!r}; defaulting to {DEFAULT_RETRY_AFTER}s")
        seconds = DEFAULT_RETRY_AFTER
    return max(0, min(seconds, MAX_RETRY_AFTER))


def discovery_get(session: requests.Session, url: str) -> requests.Response:
    """
    GET a discovery source (llms.txt / sitemap) with the same retry/backoff
    budget page fetches get.

    Discovery is fail-closed by design — a dead source aborts the whole run —
    so a single un-retried transient (one CDN 503 blip) must not be what pulls
    that trigger. Retries here, hard failure after; the caller still raises.

    Returns:
        The successful (2xx) response.

    Raises:
        requests.exceptions.RequestException: after MAX_RETRIES failures.
    """
    last_error: Exception = requests.exceptions.RequestException("no attempts made")
    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(url, headers=HEADERS, timeout=30)
            if response.status_code == 429:
                last_error = requests.exceptions.RequestException(
                    f"rate limited (429) on all {MAX_RETRIES} attempts"
                )
                if attempt < MAX_RETRIES - 1:  # no pointless sleep after the last try
                    wait_time = _retry_after_seconds(response)
                    logger.warning(f"Discovery {url}: rate limited, waiting {wait_time}s...")
                    time.sleep(wait_time)
                continue
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            last_error = e
            logger.warning(f"Discovery attempt {attempt + 1}/{MAX_RETRIES} failed for {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)
                time.sleep(delay * random.uniform(0.5, 1.0))
    raise last_error


def _reject_redirect(response, label: str) -> None:
    """
    Treat any 3xx as a fetch failure (raises RequestException).

    The shell client fetches with ``--max-redirs 0``, so a redirecting URL is
    unfetchable client-side; publishing it as ok would create permanently
    unfetchable manifest entries. Failing routes it through the normal
    retry/carry-forward path instead.
    """
    if 300 <= response.status_code < 400:
        location = response.headers.get('Location', '<no Location header>')
        logger.warning(
            f"{label}: HTTP {response.status_code} redirect -> {location} "
            f"(treated as fetch failure; client uses --max-redirs 0)"
        )
        raise requests.exceptions.RequestException(
            f"redirect {response.status_code} to {location}"
        )


def validate_markdown_content(content: str, filename: str) -> None:
    """
    Validate that content is proper markdown.

    Args:
        content: The content to validate
        filename: The filename (for error messages)

    Raises:
        ValueError: If validation fails
    """
    # Check for HTML content
    if not content or content.startswith('<!DOCTYPE') or '<html' in content[:100]:
        raise ValueError("Received HTML instead of markdown")

    # Check minimum length
    if len(content.strip()) < 50:
        raise ValueError(f"Content too short ({len(content)} bytes)")

    # Soft-404 guard: a short body with an error/maintenance phrase and no markdown
    # heading is an error page, not docs. Storing it would hash an error string as the
    # page's authoritative content (the client re-fetches the same body, gets a matching
    # sha256, and never flags it stale). Raising here routes it through carry-forward.
    if len(content.strip()) < 300 and not re.search(r'^#\s', content, re.MULTILINE):
        head = content.lower()
        soft_404_markers = (
            "page not found", "404 not found", "not found",
            "temporarily unavailable", "under maintenance",
        )
        if any(marker in head for marker in soft_404_markers):
            raise ValueError("looks like a soft-404 / error body, not documentation")

    # Check for common markdown elements
    lines = content.split('\n')
    markdown_indicators = [
        '# ',      # Headers
        '## ',
        '### ',
        '```',     # Code blocks
        '- ',      # Lists
        '* ',
        '1. ',
        '[',       # Links
        '**',      # Bold
        '_',       # Italic
        '> ',      # Quotes
    ]

    # Count markdown indicators
    indicator_count = 0
    for line in lines[:50]:  # Check first 50 lines
        for indicator in markdown_indicators:
            if line.strip().startswith(indicator) or indicator in line:
                indicator_count += 1
                break

    # The .md endpoint returns authoritative markdown; HTML and too-short content
    # are already hard-rejected above. A low indicator count only means the page is
    # sparse (e.g. a stub "overview" that is mostly links/cards) — warn, don't reject,
    # or we drop valid pages every single run.
    if indicator_count < 3:
        logger.warning(
            f"{filename}: only {indicator_count} markdown indicator(s) — sparse page, accepting"
        )

    # Check for common documentation patterns
    doc_patterns = ['installation', 'usage', 'example', 'api', 'configuration', 'claude', 'code']
    content_lower = content.lower()
    pattern_found = any(pattern in content_lower for pattern in doc_patterns)

    if not pattern_found:
        logger.warning(f"Content for {filename} doesn't contain expected documentation patterns")


def extract_title(content: Union[str, bytes]) -> str:
    """Extract the page title from markdown (first ``# `` heading), else ``"Untitled"``."""
    if isinstance(content, bytes):
        content = content.decode('utf-8', errors='replace')
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def fetch_markdown(md_url: str, session: requests.Session, label: str = "") -> bytes:
    """
    Fetch a markdown page from its verbatim ``.md`` URL.

    URLs are stored verbatim in the v2 manifest (correct host preserved), so this
    fetches exactly what discovery recorded — no base-URL reconstruction.

    Returns the RAW RESPONSE BYTES: the sha256 in the manifest must be computed
    over exactly the bytes the client's own raw fetch hashes, regardless of any
    Content-Type charset the server declares. Text-only processing (validation,
    title extraction) decodes a UTF-8 copy with errors="replace" for that purpose
    only. Redirects are NOT followed — see :func:`_reject_redirect`.

    Args:
        md_url: The verbatim ``.md`` URL to fetch.
        session: Requests session.
        label: Human-readable label for logs (usually the filename).

    Returns:
        The validated markdown content as raw bytes.

    Raises:
        Exception: On network failure after retries.
        ValueError: If the response is not valid markdown.
    """
    label = label or md_url

    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(md_url, headers=HEADERS, timeout=30, allow_redirects=False)

            if response.status_code == 429:  # Rate limited
                wait_time = _retry_after_seconds(response)
                logger.warning(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            _reject_redirect(response, label)
            response.raise_for_status()

            raw = response.content
            text = raw.decode('utf-8', errors='replace')
            validate_markdown_content(text, label)
            logger.info(f"Fetched and validated {label} ({len(raw)} bytes)")
            return raw

        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} failed for {label}: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)
                jittered_delay = delay * random.uniform(0.5, 1.0)
                time.sleep(jittered_delay)
            else:
                raise Exception(f"Failed to fetch {label} after {MAX_RETRIES} attempts: {e}")

        except ValueError as e:
            logger.error(f"Content validation failed for {label}: {e}")
            raise

    # Only reachable if every attempt returned HTTP 429 (rate limited).
    raise Exception(f"Exhausted all {MAX_RETRIES} attempts (rate limited) for {label}")


def fetch_changelog(session: requests.Session) -> Tuple[str, bytes]:
    """
    Fetch Claude Code changelog from GitHub repository.

    Args:
        session: Requests session

    Returns:
        Tuple of (filename, raw content bytes)
    """
    changelog_url = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
    filename = "changelog.md"

    logger.info(f"Fetching Claude Code changelog: {changelog_url}")

    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(changelog_url, headers=HEADERS, timeout=30, allow_redirects=False)

            if response.status_code == 429:  # Rate limited
                wait_time = _retry_after_seconds(response)
                logger.warning(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            _reject_redirect(response, filename)
            response.raise_for_status()

            content = response.content

            # v2: store the changelog VERBATIM — the exact raw bytes the client fetches
            # from the raw URL — so its manifest sha256 matches the client's and it never
            # shows as permanently "stale". Source attribution lives in the manifest's
            # url field.

            # Basic validation
            if len(content.strip()) < 100:
                raise ValueError(f"Changelog content too short ({len(content)} bytes)")

            logger.info(f"Successfully fetched changelog ({len(content)} bytes)")
            return filename, content

        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} failed for changelog: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)
                jittered_delay = delay * random.uniform(0.5, 1.0)
                logger.info(f"Retrying in {jittered_delay:.1f} seconds...")
                time.sleep(jittered_delay)
            else:
                raise Exception(f"Failed to fetch changelog after {MAX_RETRIES} attempts: {e}")

        except ValueError as e:
            logger.error(f"Changelog validation failed: {e}")
            raise

    # Only reachable if every attempt returned HTTP 429 (rate limited).
    raise Exception(f"Exhausted all {MAX_RETRIES} attempts (rate limited) for changelog")


def save_markdown_file(docs_dir: Path, filename: str, content: Union[str, bytes]) -> str:
    """
    Save markdown content (binary, byte-exact) and return its sha256.

    The file is written with the EXACT bytes that are hashed, so the manifest
    sha256 always matches what a client hashing its own raw download computes —
    no text-mode/charset re-encoding in between. str input (legacy callers/tests)
    is encoded as UTF-8 first.

    Args:
        docs_dir: Directory to save the file in
        filename: Name of the file
        content: Raw bytes to write (or str, encoded as UTF-8)

    Returns:
        SHA256 hash of the written bytes
    """
    file_path = docs_dir / filename
    data = content.encode('utf-8') if isinstance(content, str) else content

    try:
        file_path.write_bytes(data)
        content_hash = hashlib.sha256(data).hexdigest()
        logger.info(f"Saved: {filename}")
        return content_hash
    except Exception as e:
        logger.error(f"Failed to save {filename}: {e}")
        raise


def content_has_changed(content: Union[str, bytes], old_hash: str) -> bool:
    """
    Check if content has changed based on hash.

    Args:
        content: New content to check (raw bytes, or str encoded as UTF-8)
        old_hash: Previous content hash

    Returns:
        True if content has changed, False otherwise
    """
    data = content.encode('utf-8') if isinstance(content, str) else content
    new_hash = hashlib.sha256(data).hexdigest()
    return new_hash != old_hash
