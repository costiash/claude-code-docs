"""
Documentation fetcher package (v2).

Discovers the page set from the union of llms.txt + sitemaps, fetches each page's
verbatim ``.md`` into an ephemeral scratch dir, and writes a v2 manifest
(``paths_manifest.json``) at the repo root. Commits no documentation prose.

Main entry point: ``run_fetcher()`` (or the ``fetch_claude_docs.py`` wrapper).
"""

from .config import (
    SITEMAP_URLS,
    LLMS_TXT_URLS,
    MANIFEST_FILE,
    PATHS_MANIFEST_FILE,
    MANIFEST_SCHEMA_VERSION,
    DEFAULT_SCRATCH_DIR,
    ALLOWED_DOMAINS,
    HEADERS,
    MAX_RETRIES,
    RETRY_DELAY,
    MAX_RETRY_DELAY,
    RATE_LIMIT_DELAY,
    MIN_DISCOVERY_THRESHOLD,
    MAX_DELETION_PERCENT,
    MIN_EXPECTED_FILES,
)

from .manifest import (
    manifest_path,
    load_manifest,
    pages_by_url,
    build_manifest,
    save_manifest,
)

from .paths import (
    url_to_filename,
    page_id_from_filename,
    categorize_from_url,
)

from .llms_txt import (
    parse_llms_txt,
    discover_from_llms_txt,
)

from .sitemap import (
    discover_sitemap_entries,
    discover_from_all_sitemaps,
    discover_sitemap_and_base_url,
    discover_claude_code_pages,
)

from .discovery import (
    merge_discovery,
    discover_pages,
)

from .content import (
    validate_markdown_content,
    extract_title,
    fetch_markdown,
    fetch_changelog,
    save_markdown_file,
    content_has_changed,
)

from .safeguards import (
    validate_discovery_threshold,
    validate_manifest_transition,
)

from .cli import main as run_fetcher

__all__ = [
    # Config
    "SITEMAP_URLS",
    "LLMS_TXT_URLS",
    "MANIFEST_FILE",
    "PATHS_MANIFEST_FILE",
    "MANIFEST_SCHEMA_VERSION",
    "DEFAULT_SCRATCH_DIR",
    "ALLOWED_DOMAINS",
    "HEADERS",
    "MAX_RETRIES",
    "RETRY_DELAY",
    "MAX_RETRY_DELAY",
    "RATE_LIMIT_DELAY",
    "MIN_DISCOVERY_THRESHOLD",
    "MAX_DELETION_PERCENT",
    "MIN_EXPECTED_FILES",
    # Manifest
    "manifest_path",
    "load_manifest",
    "pages_by_url",
    "build_manifest",
    "save_manifest",
    # Paths
    "url_to_filename",
    "page_id_from_filename",
    "categorize_from_url",
    # llms.txt
    "parse_llms_txt",
    "discover_from_llms_txt",
    # Sitemap
    "discover_sitemap_entries",
    "discover_from_all_sitemaps",
    "discover_sitemap_and_base_url",
    "discover_claude_code_pages",
    # Discovery union
    "merge_discovery",
    "discover_pages",
    # Content
    "validate_markdown_content",
    "extract_title",
    "fetch_markdown",
    "fetch_changelog",
    "save_markdown_file",
    "content_has_changed",
    # Safeguards
    "validate_discovery_threshold",
    "validate_manifest_transition",
    # CLI
    "run_fetcher",
]
