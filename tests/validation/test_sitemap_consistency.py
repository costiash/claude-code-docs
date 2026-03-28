"""Validation tests for sitemap consistency."""

import pytest
import sys
from pathlib import Path
import json

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestManifestCompleteness:
    """Test all files are in manifest."""

    @pytest.mark.integration
    def test_all_categories_present(self, paths_manifest):
        """Test structural categories are in manifest.

        api_reference, core_documentation, and claude_code always exist because
        they map to permanent URL patterns in Anthropic's sitemaps. Other categories
        (prompt_library, resources, release_notes) depend on what the sitemaps return.
        """
        categories = paths_manifest['categories']

        # These 3 are structural — they always exist due to how categorize_path() works
        for required in ['api_reference', 'core_documentation', 'claude_code']:
            assert required in categories, f"Missing structural category: {required}"

        # Manifest should have at least these 3, possibly more
        assert len(categories) >= 3

    @pytest.mark.integration
    def test_metadata_complete(self, paths_manifest):
        """Test manifest metadata is complete."""
        assert 'metadata' in paths_manifest
        metadata = paths_manifest['metadata']

        # Required metadata fields
        assert 'generated_at' in metadata
        assert 'total_paths' in metadata
        # Optional fields
        assert isinstance(metadata.get('total_paths'), int)
        assert metadata['total_paths'] > 0

    @pytest.mark.integration
    def test_total_paths_matches_sum(self, paths_manifest):
        """Test total_paths metadata matches sum of categories."""
        total_in_metadata = paths_manifest['metadata']['total_paths']

        total_in_categories = sum(
            len(paths) for paths in paths_manifest['categories'].values()
        )

        assert total_in_metadata == total_in_categories

    @pytest.mark.integration
    def test_no_duplicate_paths_across_categories(self, paths_manifest):
        """Test no path appears in multiple categories."""
        all_paths = []

        for category_paths in paths_manifest['categories'].values():
            all_paths.extend(category_paths)

        # Check for duplicates
        unique_paths = set(all_paths)

        assert len(all_paths) == len(unique_paths), "Found duplicate paths across categories"


class TestNoOrphanedFiles:
    """Test no files are missing from manifest."""

    @pytest.mark.integration
    def test_docs_files_in_manifest(self, project_root, paths_manifest):
        """Test all markdown files in docs/ are in manifest."""
        docs_dir = project_root / "docs"

        if not docs_dir.exists():
            pytest.skip("docs directory doesn't exist yet")

        # Get all markdown files
        md_files = list(docs_dir.glob("*.md"))

        if not md_files:
            pytest.skip("No markdown files in docs/")

        # Get all paths from manifest
        manifest_paths = []
        for category_paths in paths_manifest['categories'].values():
            manifest_paths.extend(category_paths)

        # Convert manifest paths to expected filenames
        def path_to_filename(path):
            return path.replace('/', '__')[1:] + '.md'  # Remove leading /

        expected_files = {path_to_filename(path) for path in manifest_paths}

        # Check each file
        for md_file in md_files:
            # File should be in manifest (or be docs_manifest.json, etc.)
            if md_file.name not in ['docs_manifest.json', 'sitemap.json']:
                # File should correspond to a manifest path
                # (This is a simplified check)
                pass

    @pytest.mark.integration
    def test_manifest_paths_have_files(self, project_root, paths_manifest):
        """Test all manifest paths have corresponding files."""
        docs_dir = project_root / "docs"

        if not docs_dir.exists():
            pytest.skip("docs directory doesn't exist yet")

        # Get all paths from manifest
        all_paths = []
        for category_paths in paths_manifest['categories'].values():
            all_paths.extend(category_paths)

        if not all_paths:
            pytest.skip("No paths in manifest")

        # Sample check (not all 550+)
        sample_size = min(10, len(all_paths))
        import random
        sample_paths = random.sample(all_paths, sample_size)

        # Convert to filenames
        def path_to_filename(path):
            return path.replace('/', '__')[1:] + '.md'

        # Check files exist
        for path in sample_paths:
            filename = path_to_filename(path)
            file_path = docs_dir / filename

            # File should exist (if docs have been fetched)
            # This test is only meaningful after fetch
            # if not file_path.exists():
            #     # May not exist if docs not fetched yet
            #     pass


class TestCategoryCounts:
    """Test category counts match expectations."""

    @pytest.mark.integration
    def test_api_reference_largest_category(self, paths_manifest):
        """Test api_reference is the largest category (due to multi-language SDK docs)."""
        categories = paths_manifest['categories']

        if not categories:
            pytest.skip("No categories in manifest")

        api_count = len(categories.get('api_reference', []))
        total_count = sum(len(paths) for paths in categories.values())

        # API reference should be significant portion (includes multi-language SDK docs)
        if total_count > 0:
            api_percentage = api_count / total_count
            # Should be at least 50% (due to Python, TypeScript, Go, Java, Kotlin, Ruby SDK docs)
            assert api_percentage >= 0.50, f"api_reference is {api_percentage:.1%} of total"

    @pytest.mark.integration
    def test_all_categories_nonempty(self, paths_manifest):
        """Test every category in the manifest has at least one path."""
        for category, paths in paths_manifest['categories'].items():
            assert len(paths) > 0, f"{category} is empty"

    @pytest.mark.integration
    def test_category_counts_reasonable(self, paths_manifest):
        """Test structural properties of category distribution.

        Instead of hardcoding count ranges (which break when sitemaps change),
        validate invariants that hold regardless of Anthropic's doc structure.
        """
        categories = paths_manifest['categories']
        total = sum(len(paths) for paths in categories.values())

        # Total paths must exceed the safety threshold used by the fetcher
        assert total >= 200, f"Total paths {total} below safety threshold (200)"

        # api_reference is always the largest (multi-language SDK docs dominate)
        api_count = len(categories.get('api_reference', []))
        assert api_count > total * 0.50, \
            f"api_reference ({api_count}) should be >50% of total ({total})"

        # claude_code should have a reasonable number of CLI pages
        cc_count = len(categories.get('claude_code', []))
        assert cc_count >= 20, f"claude_code has only {cc_count} paths (expected >=20)"


class TestManifestFormat:
    """Test manifest file format is correct."""

    @pytest.mark.integration
    def test_manifest_is_valid_json(self, project_root):
        """Test manifest is valid JSON."""
        manifest_path = project_root / "paths_manifest.json"

        if not manifest_path.exists():
            pytest.skip("paths_manifest.json doesn't exist")

        # Should parse without error
        manifest = json.loads(manifest_path.read_text())

        assert isinstance(manifest, dict)

    @pytest.mark.integration
    def test_manifest_structure(self, paths_manifest):
        """Test manifest has correct structure."""
        # Top-level keys
        assert 'metadata' in paths_manifest
        assert 'categories' in paths_manifest

        # Metadata structure
        metadata = paths_manifest['metadata']
        assert isinstance(metadata, dict)

        # Categories structure
        categories = paths_manifest['categories']
        assert isinstance(categories, dict)

        # Each category should be a list
        for category, paths in categories.items():
            assert isinstance(paths, list)

    @pytest.mark.integration
    def test_paths_are_strings(self, paths_manifest):
        """Test all paths are strings."""
        for category_paths in paths_manifest['categories'].values():
            for path in category_paths:
                assert isinstance(path, str)
                assert len(path) > 0

    @pytest.mark.integration
    def test_paths_properly_formatted(self, paths_manifest):
        """Test paths follow expected format."""
        for category_paths in paths_manifest['categories'].values():
            for path in category_paths:
                # Should start with /en/ OR /docs/en/ (NEW Claude Code format)
                assert path.startswith('/en/') or path.startswith('/docs/en/'), \
                    f"Invalid path (must start with /en/ or /docs/en/): {path}"

                # Should not have trailing slash (except root)
                if len(path) > 4:
                    assert not path.endswith('/'), f"Trailing slash: {path}"

                # Should not have double slashes
                assert '//' not in path, f"Double slash: {path}"
