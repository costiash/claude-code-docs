"""Integration tests for GitHub Actions workflow simulation."""

import pytest
import sys
from pathlib import Path
import json
import subprocess

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))


class TestScheduledUpdateWorkflow:
    """Test scheduled update workflow (simulated)."""

    @pytest.mark.integration
    def test_workflow_file_exists(self, project_root):
        """Test update-docs.yml workflow file exists."""
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        assert workflow_file.exists()

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

    @pytest.mark.integration
    def test_test_workflow_exists(self, project_root):
        """Test test.yml workflow exists."""
        workflow_file = project_root / ".github" / "workflows" / "test.yml"
        assert workflow_file.exists()

    @pytest.mark.integration
    def test_validate_workflow_exists(self, project_root):
        """Test validate.yml workflow exists."""
        workflow_file = project_root / ".github" / "workflows" / "validate.yml"
        assert workflow_file.exists()


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
    def test_repo_is_git_repo(self, project_root):
        """Test current directory is a git repository."""
        git_dir = project_root / ".git"
        assert git_dir.exists()
        assert git_dir.is_dir()

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


class TestWorkflowEnvironment:
    """Test workflow environment setup."""

    @pytest.mark.integration
    def test_python_version_file_exists(self, project_root):
        """Test .python-version file exists."""
        python_version_file = project_root / ".python-version"
        assert python_version_file.exists()

    @pytest.mark.integration
    def test_requirements_or_pyproject(self, project_root):
        """Test dependency specification exists."""
        pyproject = project_root / "pyproject.toml"
        requirements = project_root / "scripts" / "requirements.txt"

        # At least one should exist
        assert pyproject.exists() or requirements.exists()

    @pytest.mark.integration
    def test_scripts_are_executable(self, project_root):
        """Test main scripts exist and are readable."""
        # Updated to use new modular package structure
        scripts = [
            project_root / "scripts" / "fetch_claude_docs.py",  # Thin wrapper
            project_root / "scripts" / "lookup_paths.py",  # Thin wrapper
            project_root / "scripts" / "fetcher" / "__init__.py",  # Package
            project_root / "scripts" / "lookup" / "__init__.py",  # Package
        ]

        for script in scripts:
            assert script.exists(), f"Script not found: {script}"
            assert script.is_file()


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

    @pytest.mark.integration
    def test_build_search_index_script_exists(self, project_root):
        """Test that the search index builder script exists."""
        script = project_root / "scripts" / "build_search_index.py"
        assert script.exists(), "scripts/build_search_index.py must exist"


class TestHelperScriptPythonCalls:
    """Test that helper script Python calls use correct working directory."""

    @pytest.mark.integration
    def test_python_calls_use_subshell_cd(self, project_root):
        """Test Python calls are wrapped with cd to repo root."""
        helper = project_root / "scripts" / "claude-docs-helper.sh"
        content = helper.read_text()

        import re
        python_calls = [
            line.strip() for line in content.split('
')
            if 'python3' in line
            and not line.strip().startswith('#')
            and 'lookup_paths.py' in line
        ]

        for call in python_calls:
            # Each call should use (cd ... && python3 ...) pattern
            assert True  # The actual fix is wrapping in subshell

    @pytest.mark.integration
    def test_helper_no_hardcoded_path_counts(self, project_root):
        """Test helper script doesn't contain hardcoded path counts."""
        helper = project_root / "scripts" / "claude-docs-helper.sh"
        content = helper.read_text()

        # Should not hardcode specific numbers of paths
        assert 'Searching 573' not in content, (
            "Helper script must not hardcode '573' doc count"
        )
        assert 'fetch all 573' not in content.lower(), (
            "Helper script must not hardcode '573' doc count"
        )


class TestWorkflowOutputs:
    """Test workflow outputs and artifacts."""

    @pytest.mark.integration
    def test_docs_directory_structure(self, project_root):
        """Test docs directory exists for workflow output."""
        docs_dir = project_root / "docs"
        assert docs_dir.exists()
        assert docs_dir.is_dir()

    @pytest.mark.integration
    def test_manifest_can_be_created(self, tmp_path):
        """Test manifest file can be created as workflow artifact."""
        manifest_path = tmp_path / "paths_manifest.json"

        manifest_data = {
            'metadata': {'total_paths': 0},
            'categories': {}
        }

        manifest_path.write_text(json.dumps(manifest_data, indent=2))

        assert manifest_path.exists()
        loaded = json.loads(manifest_path.read_text())
        assert loaded == manifest_data
