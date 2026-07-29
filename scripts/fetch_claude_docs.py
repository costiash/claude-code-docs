#!/usr/bin/env python3
"""
Claude Code documentation fetcher (v2) — thin wrapper.

The implementation lives in the ``fetcher`` package:

- fetcher/config.py     - Configuration constants and thresholds
- fetcher/llms_txt.py   - llms.txt parsing
- fetcher/sitemap.py    - Sitemap discovery (URLs + lastmod)
- fetcher/discovery.py  - Union of llms.txt + sitemap into the page set
- fetcher/paths.py      - URL → filename / category / id mapping
- fetcher/content.py    - Verbatim .md fetching and validation
- fetcher/manifest.py   - v2 manifest read/write
- fetcher/safeguards.py - Discovery + manifest-transition safeguards
- fetcher/cli.py        - Main entry point

The public API is re-exported here for backwards compatibility (single source of
truth: ``fetcher.__all__``).
"""

from fetcher import *  # noqa: F401,F403  (backwards-compat re-export of fetcher.__all__)
from fetcher import run_fetcher as main

if __name__ == "__main__":
    main()
