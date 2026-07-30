"""
Configuration constants for the documentation fetcher.

This module contains all configuration values, URLs, and thresholds
used throughout the fetcher package.
"""

import logging

# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


# =============================================================================
# SITEMAP URLS - Documentation sources (verified live 2026-07-31)
# =============================================================================
# platform.claude.com and code.claude.com are the two canonical doc domains.
# docs.claude.com and docs.anthropic.com are LEGACY ALIASES that now 301-redirect
# here (by content type: CLI pages -> code.claude.com, everything else ->
# platform.claude.com). Discover from the canonical hosts, never the aliases — a
# stored 301 URL would drift both the host and the sha256. (They returned 500/401
# back in Dec 2025; they now redirect. Either way they are not discovery sources.)
SITEMAP_URLS = [
    "https://platform.claude.com/sitemap.xml",   # API, Agent SDK, Core docs, Prompt Library
    "https://code.claude.com/docs/sitemap.xml",  # Claude Code CLI documentation
]
# NOT discovery sources: docs.claude.com, docs.anthropic.com (301 redirect aliases)

# llms.txt sources — markdown lists of "title + .md URL + description" per page.
# Used together with the sitemaps (union discovery): llms.txt supplies titles,
# descriptions, and coverage the sitemap-only path (e.g. agent-sdk) fetch missed;
# the sitemap supplies <lastmod>. See scripts/fetcher/discovery.py.
LLMS_TXT_URLS = [
    "https://code.claude.com/docs/llms.txt",     # Claude Code + Agent SDK (on code.claude.com)
    "https://platform.claude.com/llms.txt",      # Platform API, guides, prompt library
]


# =============================================================================
# FILE CONFIGURATION
# =============================================================================
MANIFEST_FILE = "docs_manifest.json"  # legacy v1 manifest (docs/); removed in cutover

# v2 manifest (repo root, single source of truth) — see scripts/fetcher/manifest.py
MANIFEST_SCHEMA_VERSION = 2
PATHS_MANIFEST_FILE = "paths_manifest.json"

# Ephemeral scratch dir the v2 fetcher writes .md into (to hash + feed the index).
# Never committed; overridable so Verify runs don't churn the tracked docs/ tree.
DEFAULT_SCRATCH_DIR = ".doc_fetch"

# Domains the fetcher (and the client fetch layer, B1) are allowed to request.
ALLOWED_DOMAINS = (
    "code.claude.com",
    "platform.claude.com",
    "raw.githubusercontent.com",  # changelog.md source
)


# =============================================================================
# HTTP REQUEST CONFIGURATION
# =============================================================================
# Headers to bypass caching and identify the script
HEADERS = {
    'User-Agent': 'Claude-Code-Docs-Fetcher/3.0',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}


# =============================================================================
# RETRY CONFIGURATION
# =============================================================================
MAX_RETRIES = 3
RETRY_DELAY = 2  # initial delay in seconds
MAX_RETRY_DELAY = 30  # maximum delay in seconds
RATE_LIMIT_DELAY = 0.5  # seconds between requests


# =============================================================================
# SAFETY THRESHOLDS - Prevent catastrophic deletion from sitemap failures
# =============================================================================
MIN_DISCOVERY_THRESHOLD = 200      # Refuse to proceed if < 200 paths discovered
MAX_DELETION_PERCENT = 10          # Never delete > 10% of existing files
MIN_EXPECTED_FILES = 250           # Minimum expected file count after fetch
