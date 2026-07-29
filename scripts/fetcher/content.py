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
from typing import Tuple

import requests

from .config import (
    HEADERS,
    MAX_RETRIES,
    RETRY_DELAY,
    MAX_RETRY_DELAY,
    logger,
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


def extract_title(content: str) -> str:
    """Extract the page title from markdown (first ``# `` heading), else ``"Untitled"``."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def fetch_markdown(md_url: str, session: requests.Session, label: str = "") -> str:
    """
    Fetch a markdown page from its verbatim ``.md`` URL.

    URLs are stored verbatim in the v2 manifest (correct host preserved), so this
    fetches exactly what discovery recorded — no base-URL reconstruction.

    Args:
        md_url: The verbatim ``.md`` URL to fetch.
        session: Requests session.
        label: Human-readable label for logs (usually the filename).

    Returns:
        The validated markdown content.

    Raises:
        Exception: On network failure after retries.
        ValueError: If the response is not valid markdown.
    """
    label = label or md_url

    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(md_url, headers=HEADERS, timeout=30, allow_redirects=True)

            if response.status_code == 429:  # Rate limited
                wait_time = int(response.headers.get('Retry-After', 60))
                logger.warning(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

            content = response.text
            validate_markdown_content(content, label)
            logger.info(f"Fetched and validated {label} ({len(content)} bytes)")
            return content

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


def fetch_changelog(session: requests.Session) -> Tuple[str, str]:
    """
    Fetch Claude Code changelog from GitHub repository.

    Args:
        session: Requests session

    Returns:
        Tuple of (filename, content)
    """
    changelog_url = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
    filename = "changelog.md"

    logger.info(f"Fetching Claude Code changelog: {changelog_url}")

    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(changelog_url, headers=HEADERS, timeout=30, allow_redirects=True)

            if response.status_code == 429:  # Rate limited
                wait_time = int(response.headers.get('Retry-After', 60))
                logger.warning(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

            content = response.text

            # v2: store the changelog VERBATIM — the exact bytes the client fetches from
            # the raw URL — so its manifest sha256 matches the client's and it never shows
            # as permanently "stale". Source attribution lives in the manifest's url field.

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


def save_markdown_file(docs_dir: Path, filename: str, content: str) -> str:
    """
    Save markdown content and return its hash.

    Args:
        docs_dir: Directory to save the file in
        filename: Name of the file
        content: Content to write

    Returns:
        SHA256 hash of the content
    """
    file_path = docs_dir / filename

    try:
        file_path.write_text(content, encoding='utf-8')
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        logger.info(f"Saved: {filename}")
        return content_hash
    except Exception as e:
        logger.error(f"Failed to save {filename}: {e}")
        raise


def content_has_changed(content: str, old_hash: str) -> bool:
    """
    Check if content has changed based on hash.

    Args:
        content: New content to check
        old_hash: Previous content hash

    Returns:
        True if content has changed, False otherwise
    """
    new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return new_hash != old_hash
