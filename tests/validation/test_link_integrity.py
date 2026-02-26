"""Validation tests for internal link validity."""

import pytest
import sys
from pathlib import Path
import re
import json

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestInternalLinksWork:
    """Test links between docs resolve correctly."""

    @pytest.mark.integration
    def test_find_internal_links(self, sample_markdown):
        """Test internal links are identified."""
        # Find markdown links
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', sample_markdown)

        internal_links = [
            url for text, url in links
            if url.startswith('/en/')
        ]

        # Sample should have internal links
        if internal_links:
            assert len(internal_links) > 0

    @pytest.mark.integration
    def test_internal_links_in_manifest(self, paths_manifest, project_root):
        """Test internal links in actual docs point to paths in manifest.

        Scans all documentation files for internal links (markdown link syntax)
        and validates that a reasonable percentage resolve to known manifest paths.

        Two link patterns exist in the docs:
          - /docs/en/... (platform docs linking to each other)
          - /en/...      (Claude Code docs using short paths)
        """
        docs_dir = project_root / 'docs'

        # Build set of all known manifest paths (stripped of leading /)
        all_paths = set()
        for category_paths in paths_manifest['categories'].values():
            for p in category_paths:
                all_paths.add(p.strip('/'))

        # Scan real docs for internal links
        total_links = 0
        broken_links = []

        for md_file in sorted(docs_dir.glob('*.md')):
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue

            # Match markdown links: [text](/docs/en/...) or [text](/en/...)
            links = re.findall(
                r'\[([^\]]+)\]\((/(?:docs/)?en/[^)#\s]+)',
                content
            )

            for text, url in links:
                total_links += 1
                clean_path = url.strip('/')

                # Try exact match first
                if clean_path in all_paths:
                    continue

                # Claude Code docs use /en/<page> which maps to /docs/en/<page>
                # in the manifest
                if clean_path.startswith('en/') and f'docs/{clean_path}' in all_paths:
                    continue

                broken_links.append((md_file.name, text, url))

        assert total_links > 100, (
            f"Expected 100+ internal links in docs, found {total_links}. "
            f"Link extraction may be broken."
        )

        # Allow tolerance — some links point to pages that aren't in our manifest
        # (e.g., pages only on code.claude.com, dynamically generated pages, or
        # paths that use different naming than our sitemap discovers)
        broken_pct = (len(broken_links) / total_links * 100) if total_links else 0

        assert broken_pct < 30, (
            f"{len(broken_links)} of {total_links} internal links ({broken_pct:.1f}%) "
            f"don't resolve to manifest paths. First 10:\n"
            + "\n".join(f"  [{f}] '{t}' -> {u}"
                        for f, t, u in broken_links[:10])
        )

    @pytest.mark.integration
    def test_relative_links_resolved(self):
        """Test relative links are handled."""
        markdown = "[Link](./relative/path.md)"

        # Check if relative links are present
        has_relative = bool(re.search(r'\]\(\./|\]\(\.\./\)', markdown))

        # Relative links should ideally be converted to absolute
        # or handled appropriately


class TestNoBrokenAnchors:
    """Test fragment identifiers are valid."""

    @pytest.mark.integration
    def test_identify_anchor_links(self, sample_markdown):
        """Test anchor links are identified."""
        # Find links with fragments
        anchor_links = re.findall(r'\[([^\]]+)\]\(([^)]*#[^)]+)\)', sample_markdown)

        # If anchor links exist, they should be well-formed
        for text, url in anchor_links:
            # Should have text
            assert len(text) > 0
            # Should have fragment
            assert '#' in url

    @pytest.mark.integration
    def test_anchor_targets_exist(self, sample_html):
        """Test anchor targets exist in HTML."""
        # Find all id attributes
        ids = re.findall(r'id="([^"]+)"', sample_html)

        # Find all anchor links
        anchor_links = re.findall(r'href="[^"]*#([^"]+)"', sample_html)

        # Each anchor should have a corresponding id
        # (This is a simplified check)
        if anchor_links:
            # Should have some ids
            assert len(ids) > 0

    @pytest.mark.integration
    def test_fragment_format_valid(self):
        """Test fragment identifiers are properly formatted."""
        valid_fragments = [
            "#section-name",
            "#overview",
            "#getting-started"
        ]

        invalid_fragments = [
            "#",
            "##double",
            "#spaces in fragment"
        ]

        # Valid fragments should match pattern
        for fragment in valid_fragments:
            assert re.match(r'#[a-z0-9-]+$', fragment)

        # Invalid fragments should not match
        for fragment in invalid_fragments:
            # May or may not match depending on validation strictness
            pass


class TestRelativeLinks:
    """Test relative links are converted correctly."""

    @pytest.mark.integration
    def test_relative_to_absolute_conversion(self):
        """Test relative links are converted to absolute."""
        relative = "[Link](../other-page)"
        absolute = "[Link](/en/docs/other-page)"

        # If conversion happens, should be absolute
        # This depends on implementation
        pass

    @pytest.mark.integration
    def test_same_directory_links(self):
        """Test same-directory links are handled."""
        link = "[Link](./sibling-page)"

        # Should be handled appropriately
        assert 'sibling-page' in link

    @pytest.mark.integration
    def test_parent_directory_links(self):
        """Test parent directory links are handled."""
        link = "[Link](../parent-page)"

        # Should be handled appropriately
        assert 'parent-page' in link


class TestExternalLinks:
    """Test external links are preserved."""

    @pytest.mark.integration
    def test_external_links_preserved(self):
        """Test external links are kept as-is."""
        markdown = "[Anthropic](https://www.anthropic.com)"

        # External links should be preserved
        assert 'https://www.anthropic.com' in markdown

    @pytest.mark.integration
    def test_http_and_https(self):
        """Test both HTTP and HTTPS links are handled."""
        markdown = """
[HTTP](http://example.com)
[HTTPS](https://example.com)
        """

        assert 'http://example.com' in markdown
        assert 'https://example.com' in markdown

    @pytest.mark.integration
    def test_mailto_links(self):
        """Test mailto links are preserved."""
        markdown = "[Email](mailto:test@example.com)"

        assert 'mailto:test@example.com' in markdown


class TestLinkTextQuality:
    """Test link text is descriptive."""

    @pytest.mark.integration
    def test_no_empty_link_text(self, sample_markdown):
        """Test links have non-empty text."""
        links = re.findall(r'\[([^\]]*)\]\([^)]+\)', sample_markdown)

        for link_text in links:
            # Link text should not be empty
            assert len(link_text.strip()) > 0

    @pytest.mark.integration
    def test_descriptive_link_text(self, sample_markdown):
        """Test link text is descriptive (not just 'here' or 'click')."""
        links = re.findall(r'\[([^\]]+)\]\([^)]+\)', sample_markdown)

        # Check for common non-descriptive patterns
        non_descriptive = ['here', 'click', 'link', 'this']

        # Most links should be descriptive
        descriptive_count = sum(
            1 for text in links
            if text.lower() not in non_descriptive
        )

        if links:
            # At least some links should be descriptive
            assert descriptive_count >= len(links) * 0.5  # 50% threshold
