"""Integration tests for GitHub Actions workflow simulation."""

import pytest
import re
import sys
from pathlib import Path
import subprocess

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestScheduledUpdateWorkflow:
    """Test scheduled update workflow (simulated)."""

    @pytest.mark.integration
    def test_workflow_syntax_valid(self, project_root):
        """Test workflow file has valid YAML syntax."""
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"

        # Try to parse YAML
        import yaml
        try:
            with open(workflow_file) as f:
                workflow_data = yaml.safe_load(f)

            assert workflow_data is not None
            assert 'name' in workflow_data
            # YAML parses 'on:' as True (boolean key)
            assert 'on' in workflow_data or True in workflow_data
        except ImportError:
            # If PyYAML not available, just check file is readable
            content = workflow_file.read_text()
            assert len(content) > 0


class TestManualTrigger:
    """Test manual workflow trigger (workflow_dispatch)."""

    @pytest.mark.integration
    def test_workflow_has_manual_trigger(self, project_root):
        """Test workflow supports manual triggering."""
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        # Check for workflow_dispatch
        assert 'workflow_dispatch' in content


class TestCommitAndPush:
    """Test git commit and push simulation."""

    @pytest.mark.integration
    def test_git_available(self):
        """Test git is available in environment."""
        try:
            result = subprocess.run(
                ['git', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            assert result.returncode == 0
        except FileNotFoundError:
            pytest.skip("git not available")

    @pytest.mark.integration
    def test_can_check_git_status(self, project_root):
        """Test can check git status."""
        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            # Should succeed (return code 0)
            assert result.returncode == 0
        except FileNotFoundError:
            pytest.skip("git not available")


class TestManifestStaging:
    """Test that CI/CD stages all required files."""

    @pytest.mark.integration
    def test_workflow_stages_paths_manifest(self, project_root):
        """Test that update-docs workflow stages paths_manifest.json (not just docs/)."""
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        # The git add command must include paths_manifest.json
        # It should NOT be just "git add -A docs/"
        assert 'paths_manifest.json' in content, (
            "Workflow must stage paths_manifest.json — currently only stages docs/"
        )


class TestSearchIndexGeneration:
    """Test that CI/CD generates search index."""

    @pytest.mark.integration
    def test_workflow_builds_search_index(self, project_root):
        """Test that update-docs workflow runs build_search_index.py."""
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        assert 'build_search_index.py' in content, (
            "Workflow must run build_search_index.py to generate .search_index.json"
        )


class TestSafeguardParity:
    """Test that workflow shell safeguards stay in sync with the Python fetcher config."""

    @pytest.mark.integration
    def test_workflow_page_floor_matches_fetcher_config(self, project_root):
        """The jq page-count floor in update-docs.yml must equal MIN_EXPECTED_FILES.

        update-docs.yml repeats the minimum-file-count floor as a belt-and-suspenders
        jq check ([ "$COUNT" -lt N ]) before committing. If it drifts from
        scripts/fetcher/config.py MIN_EXPECTED_FILES, one guard silently weakens.
        """
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        match = re.search(r'"\$COUNT"\s+-lt\s+(\d+)', content)
        assert match, (
            "update-docs.yml must contain the page-count floor check "
            '(if [ "$COUNT" -lt <N> ])'
        )
        workflow_floor = int(match.group(1))

        from fetcher.config import MIN_EXPECTED_FILES
        assert workflow_floor == MIN_EXPECTED_FILES, (
            f"Workflow jq floor ({workflow_floor}) drifted from "
            f"fetcher.config.MIN_EXPECTED_FILES ({MIN_EXPECTED_FILES})"
        )


class TestWorkflowOutputs:
    """Test workflow outputs and artifacts."""

    @pytest.mark.integration
    def test_committed_data_files_exist(self, project_root):
        """v2 workflow output is the committed manifest + prose-free index (docs/ is gone)."""
        assert (project_root / "paths_manifest.json").is_file()
        assert (project_root / "search_index.json").is_file()
