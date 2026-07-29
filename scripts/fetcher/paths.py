"""
URL → filename / category / id mapping (v2).

In v2 the manifest stores URLs **verbatim** from discovery, so there is no more
base-URL reconstruction, no hardcoded CLI page set, and no legacy path
conversion. This module only maps a canonical page URL to:

- a flattened cache filename (the existing convention, so plugin globs survive),
- a stable page id, and
- a category drawn from the vocabulary in
  ``plugin/skills/claude-docs/manifest-reference.md`` (the skills' source of truth).

Filename convention (kept identical to v1 for existing pages):
- ``code.claude.com`` pages → ``claude-code__<subpath>.md`` where ``<subpath>`` is
  everything after ``/docs/en/`` with ``/`` → ``__``. Using the full sub-path
  (not just the last segment) is required now that agent-sdk pages live on
  code.claude.com — otherwise ``agent-sdk/overview`` and top-level ``overview``
  would collide.
- ``platform.claude.com`` pages → ``<path>.md`` with leading ``/`` stripped and
  ``/`` → ``__`` (yields the existing ``docs__en__...`` names).
"""

from urllib.parse import urlparse

_CODE_HOST = "code.claude.com"
_CODE_PREFIX = "/docs/en"  # code.claude.com page slugs follow this


def url_to_filename(url: str) -> str:
    """
    Convert a canonical page URL to its flattened cache filename.

    Raises:
        ValueError: If the URL has no page slug (e.g. the bare ``/docs/en/`` root)
            or otherwise produces an empty/invalid filename.
    """
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")

    if parsed.netloc == _CODE_HOST:
        if path.startswith(_CODE_PREFIX + "/"):
            rest = path[len(_CODE_PREFIX) + 1:]
        elif path == _CODE_PREFIX:
            rest = ""
        else:
            rest = path.lstrip("/")
        if not rest:
            raise ValueError(f"URL produces empty filename (no page slug): {url}")
        safe = "claude-code__" + rest.replace("/", "__")
    else:
        rest = path.lstrip("/")
        if not rest:
            raise ValueError(f"URL produces empty filename (no page slug): {url}")
        safe = rest.replace("/", "__")

    # Sanitize: only alphanumerics, hyphen, underscore, dot (path-traversal safe).
    safe = "".join(c for c in safe if c.isalnum() or c in "-_.")

    if not safe or safe == ".md":
        raise ValueError(f"URL produces empty filename: {url}")
    if not safe.endswith(".md"):
        safe += ".md"
    return safe


def page_id_from_filename(filename: str) -> str:
    """Derive a stable page id from a filename: ``claude-code__hooks.md`` → ``claude-code/hooks``."""
    stem = filename[:-3] if filename.endswith(".md") else filename
    return stem.replace("__", "/")


def categorize_from_url(url: str) -> str:
    """
    Categorize a page from its host + path, using the manifest-reference vocabulary.

    Returns one of: claude_code, agent_sdk, api_reference, agents_and_tools,
    about_claude, test_and_evaluate, prompt_library, resources, release_notes,
    get_started, core_documentation.
    """
    parsed = urlparse(url)
    host = parsed.netloc
    path = parsed.path

    # Reduce "/docs/en/<section>/..." (or "/en/<section>/...") to "/<section>/...".
    sub = path
    for prefix in ("/docs/en", "/en"):
        if path == prefix:
            sub = "/"
            break
        if path.startswith(prefix + "/"):
            sub = path[len(prefix):]
            break

    if host == _CODE_HOST:
        return "agent_sdk" if sub.startswith("/agent-sdk/") else "claude_code"

    # platform.claude.com
    if sub.startswith("/api/"):
        return "api_reference"
    if sub.startswith("/agent-sdk/"):
        return "agent_sdk"
    if sub.startswith("/agents-and-tools/"):
        return "agents_and_tools"
    if sub.startswith("/about-claude/"):
        return "about_claude"
    if sub.startswith("/test-and-evaluate/"):
        return "test_and_evaluate"
    if sub.startswith("/resources/prompt-library/"):
        return "prompt_library"
    if sub.startswith("/resources/"):
        return "resources"
    if sub.startswith("/release-notes/"):
        return "release_notes"
    if sub == "/get-started" or sub.startswith("/get-started"):
        return "get_started"
    return "core_documentation"
