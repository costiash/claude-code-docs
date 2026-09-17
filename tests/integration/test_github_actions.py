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

        update-docs.yml repeats the fetched-ok floor as a belt-and-suspenders
        jq check ([ "$OK_DOCS" -lt N ]) before committing. If it drifts from
        scripts/fetcher/config.py MIN_EXPECTED_FILES, one guard silently weakens.
        """
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        match = re.search(r'"\$OK_DOCS"\s+-lt\s+(\d+)', content)
        assert match, (
            "update-docs.yml must contain the fetched-ok floor check "
            '(if [ "$OK_DOCS" -lt <N> ])'
        )
        workflow_floor = int(match.group(1))

        from fetcher.config import MIN_EXPECTED_FILES
        assert workflow_floor == MIN_EXPECTED_FILES, (
            f"Workflow jq floor ({workflow_floor}) drifted from "
            f"fetcher.config.MIN_EXPECTED_FILES ({MIN_EXPECTED_FILES})"
        )

    @pytest.mark.integration
    def test_workflow_stale_ceiling_matches_fetcher_config(self, project_root):
        """The jq stale-share ceiling in update-docs.yml must equal MAX_STALE_PERCENT.

        The workflow mirrors the Python stale-share guard as integer arithmetic
        ([ $((NOT_OK * 100)) -gt $((DOCS * N)) ]). If N drifts from
        scripts/fetcher/config.py MAX_STALE_PERCENT, one guard silently weakens.
        """
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        match = re.search(r"\$\(\(DOCS\s*\*\s*(\d+)\)\)", content)
        assert match, (
            "update-docs.yml must contain the stale-share ceiling check "
            "([ $((NOT_OK * 100)) -gt $((DOCS * <N>)) ])"
        )
        workflow_ceiling = int(match.group(1))

        from fetcher.config import MAX_STALE_PERCENT
        assert workflow_ceiling == MAX_STALE_PERCENT, (
            f"Workflow jq stale ceiling ({workflow_ceiling}) drifted from "
            f"fetcher.config.MAX_STALE_PERCENT ({MAX_STALE_PERCENT})"
        )

    @pytest.mark.integration
    def test_workflow_confirm_removals_input_is_wired_to_env(self, project_root):
        """The override reaches both consumers only through the dispatch input.

        cli.py reads DOCS_CONFIRM_REMOVALS during the fetch step; the jq mirror
        reads it during the safeguard step. Each step's env must derive from
        `inputs.confirm_removals` (a declared boolean input), and the expression
        must yield '0' when the input is absent (scheduled runs). The expression
        itself can only be evaluated by GitHub; this pins the wiring.
        """
        import yaml
        wf = yaml.safe_load((project_root / ".github" / "workflows" / "update-docs.yml").read_text())
        on = wf.get("on") or wf.get(True)
        inp = on["workflow_dispatch"]["inputs"]["confirm_removals"]
        assert inp["type"] == "boolean" and inp["default"] is False

        steps = {s.get("name", ""): s for s in wf["jobs"]["update-docs"]["steps"]}
        fetch = steps["Fetch latest documentation (v2 manifest)"]
        guard = next(s for n, s in steps.items() if n.startswith("Safeguard"))
        for step in (fetch, guard):
            expr = step["env"]["DOCS_CONFIRM_REMOVALS"]
            assert "inputs.confirm_removals" in expr, expr
            assert "'1' || '0'" in expr, expr  # falls back to '0' on schedule

    @pytest.mark.integration
    def test_workflow_removal_ceiling_matches_fetcher_config(self, project_root):
        """The jq live-removal ceiling in update-docs.yml must equal MAX_DELETION_PERCENT.

        The workflow diffs HEAD's manifest against the new one and aborts when
        more than N% of previously-live pages vanished
        ([ $((REMOVED_LIVE * 100)) -gt $((OLD_LIVE * N)) ]). If N drifts from
        scripts/fetcher/config.py MAX_DELETION_PERCENT, one guard silently weakens.
        """
        workflow_file = project_root / ".github" / "workflows" / "update-docs.yml"
        content = workflow_file.read_text()

        match = re.search(r"\$\(\(OLD_LIVE\s*\*\s*(\d+)\)\)", content)
        assert match, (
            "update-docs.yml must contain the live-removal ceiling check "
            "([ $((REMOVED_LIVE * 100)) -gt $((OLD_LIVE * <N>)) ])"
        )
        workflow_ceiling = int(match.group(1))

        from fetcher.config import MAX_DELETION_PERCENT
        assert workflow_ceiling == MAX_DELETION_PERCENT, (
            f"Workflow jq removal ceiling ({workflow_ceiling}) drifted from "
            f"fetcher.config.MAX_DELETION_PERCENT ({MAX_DELETION_PERCENT})"
        )


class TestSafeguardStepExecution:
    """Execute the workflow's jq safeguard step body against synthetic manifests.

    The parity tests above pin the constants; this class proves the step's
    arithmetic and jq behave like the Python guard at the boundaries. The body
    is extracted from the YAML so the test never drifts from the real step, and
    it runs under ``bash -e`` in a throwaway git repo with the "old" manifest
    committed at HEAD, exactly as actions/checkout leaves it.
    """

    @staticmethod
    def _step_body(project_root):
        import yaml
        wf = yaml.safe_load(
            (project_root / ".github" / "workflows" / "update-docs.yml").read_text()
        )
        steps = [s for s in wf["jobs"]["update-docs"]["steps"] if s.get("name", "").startswith("Safeguard")]
        assert len(steps) == 1, "expected exactly one Safeguard step"
        return steps[0]["run"]

    @staticmethod
    def _pages(ok=0, stale=0, prefix="u"):
        return [
            {"id": f"{prefix}{i}", "url": f"https://code.claude.com/docs/en/{prefix}{i}", "fetch_status": "ok"}
            for i in range(ok)
        ] + [
            {"id": f"{prefix}s{i}", "url": f"https://code.claude.com/docs/en/{prefix}s{i}", "fetch_status": "stale"}
            for i in range(stale)
        ]

    def _run(self, project_root, tmp_path, old_pages, new_pages, commit_old=True, old_raw=None, extra_env=None):
        """old_raw, when given, is committed verbatim at HEAD instead of a v2 manifest."""
        import json
        env = {"PATH": __import__("os").environ["PATH"], "HOME": str(tmp_path), **(extra_env or {})}
        repo = tmp_path / "repo"
        repo.mkdir()
        git = lambda *a: subprocess.run(["git", *a], cwd=repo, env=env, check=True, capture_output=True)
        git("init", "-q")
        git("config", "user.email", "t@example.com")
        git("config", "user.name", "t")
        if commit_old:
            old_text = old_raw if old_raw is not None else json.dumps({"schema_version": 2, "pages": old_pages})
            (repo / "paths_manifest.json").write_text(old_text)
            git("add", "paths_manifest.json")
            git("commit", "-q", "-m", "old")
        else:
            (repo / ".keep").write_text("")
            git("add", ".keep")
            git("commit", "-q", "-m", "empty")
        (repo / "paths_manifest.json").write_text(json.dumps({"schema_version": 2, "pages": new_pages}))
        return subprocess.run(
            ["bash", "-e", "-c", self._step_body(project_root)],
            cwd=repo, env=env, capture_output=True, text=True, timeout=60,
        )

    @pytest.mark.integration
    def test_step_passes_when_only_stale_pages_leave(self, project_root, tmp_path):
        # The 2026-09-10 shape: 300 ok + 133 stale at HEAD, new run keeps the 300 ok.
        old = self._pages(ok=300, stale=133)
        new = self._pages(ok=300)
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode == 0, r.stdout + r.stderr
        assert "Previously-live pages removed: 0 of 300" in r.stdout

    @pytest.mark.integration
    def test_step_aborts_when_live_removal_exceeds_ceiling(self, project_root, tmp_path):
        old = self._pages(ok=300, stale=133)
        new = self._pages(ok=300)[31:]  # 31/300 = 10.3% of live pages
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode != 0
        assert "previously-live pages removed (>10%)" in r.stdout

    @pytest.mark.integration
    def test_step_confirm_removals_override_allows_over_ceiling(self, project_root, tmp_path):
        old = self._pages(ok=300, stale=133)
        new = self._pages(ok=300)[31:]  # 10.3% of live pages
        r = self._run(project_root, tmp_path, old, new, extra_env={"DOCS_CONFIRM_REMOVALS": "1"})
        assert r.returncode == 0, r.stdout + r.stderr
        assert "::warning::" in r.stdout and "allowed by the confirm_removals override" in r.stdout
        assert r.stdout.count("  removed: ") == 31, r.stdout

    @pytest.mark.integration
    def test_step_override_listing_matches_count_with_duplicate_dead_rows(self, project_root, tmp_path):
        # A URL that also has a stale row is dead: it must be neither counted nor
        # listed. 400 ok, 5 of them duplicated as stale; drop the first 100 ok
        # (300 remain, clearing the floor so the override path is what runs).
        old = self._pages(ok=400) + [dict(p, fetch_status="stale") for p in self._pages(ok=5)]
        new = self._pages(ok=400)[100:]
        r = self._run(project_root, tmp_path, old, new, extra_env={"DOCS_CONFIRM_REMOVALS": "1"})
        assert r.returncode == 0, r.stdout + r.stderr
        assert "Previously-live pages removed: 95 of 395" in r.stdout
        assert r.stdout.count("  removed: ") == 95, r.stdout

    @pytest.mark.integration
    def test_step_confirm_removals_override_does_not_bypass_other_guards(self, project_root, tmp_path):
        r = self._run(project_root, tmp_path, self._pages(ok=300), self._pages(ok=249),
                      extra_env={"DOCS_CONFIRM_REMOVALS": "1"})
        assert r.returncode != 0 and "(<250)" in r.stdout

    @pytest.mark.integration
    def test_step_passes_at_exact_live_removal_ceiling(self, project_root, tmp_path):
        old = self._pages(ok=300, stale=133)
        new = self._pages(ok=300)[30:]  # 30/300 = exactly 10%: strict > passes
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode == 0, r.stdout + r.stderr

    @pytest.mark.integration
    def test_step_aborts_when_stale_share_exceeds_ceiling(self, project_root, tmp_path):
        # Same URL set at HEAD and now (no removals), 101 of 401 carried forward.
        old = self._pages(ok=401)
        new = self._pages(ok=300) + self._pages(ok=401)[300:]
        for p in new[300:]:
            p["fetch_status"] = "stale"  # 101/401 = 25.2%
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode != 0
        assert "stale/failed (>25%)" in r.stdout

    @pytest.mark.integration
    def test_step_passes_at_exact_stale_ceiling(self, project_root, tmp_path):
        # Same URL set at HEAD and now (no removals), 100 of 400 carried forward.
        old = self._pages(ok=400)
        new = self._pages(ok=400)
        for p in new[300:]:
            p["fetch_status"] = "stale"  # 100/400 = exactly 25%
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode == 0, r.stdout + r.stderr

    @pytest.mark.integration
    def test_step_aborts_below_page_floor(self, project_root, tmp_path):
        r = self._run(project_root, tmp_path, self._pages(ok=300), self._pages(ok=249))
        assert r.returncode != 0
        assert "(<250)" in r.stdout

    @pytest.mark.integration
    def test_step_floor_counts_ok_pages_not_total(self, project_root, tmp_path):
        # 300 entries but only 249 fetched ok: the Python floor aborts, so must the mirror.
        old = self._pages(ok=300)
        new = self._pages(ok=300)
        for p in new[249:]:
            p["fetch_status"] = "stale"
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode != 0
        assert "(<250)" in r.stdout

    @pytest.mark.integration
    def test_step_skips_removal_check_without_head_manifest(self, project_root, tmp_path):
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), commit_old=False)
        assert r.returncode == 0, r.stdout + r.stderr
        assert "skipping live-removal check" in r.stdout

    @pytest.mark.integration
    def test_step_skips_removal_check_for_non_v2_head_manifest(self, project_root, tmp_path):
        # A legacy (non-v2) manifest at HEAD is "empty" to load_manifest(); same here.
        legacy = '{"metadata": {"version": 1}, "categories": {}}'
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), old_raw=legacy)
        assert r.returncode == 0, r.stdout + r.stderr
        assert "skipping live-removal check" in r.stdout

    @pytest.mark.integration
    def test_step_fails_closed_on_unparsable_head_manifest(self, project_root, tmp_path):
        # load_manifest() refuses to proceed on corrupt JSON; the mirror must too.
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), old_raw="{not json")
        assert r.returncode != 0
        assert "not a valid JSON object" in r.stdout

    @pytest.mark.integration
    def test_step_fails_closed_on_empty_head_manifest(self, project_root, tmp_path):
        # jq 1.6 exits 0 on empty input; the step must not read that as "valid".
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), old_raw="")
        assert r.returncode != 0
        assert "not a valid JSON object" in r.stdout

    @pytest.mark.integration
    def test_step_duplicate_url_with_any_dead_row_is_dead(self, project_root, tmp_path):
        # Mirrors the Python set logic: one stale row makes the URL dead even if an
        # ok row for the same URL also exists, so dropping it is not a live removal.
        old = self._pages(ok=300) + [dict(p, fetch_status="stale") for p in self._pages(ok=31)]
        new = self._pages(ok=300)[31:]
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode == 0, r.stdout + r.stderr
        assert "Previously-live pages removed: 0 of 269" in r.stdout

    @pytest.mark.integration
    def test_step_ignores_non_string_or_empty_urls(self, project_root, tmp_path):
        # Same rule as the Python guard: a numeric or empty url is ignored, not
        # counted as a live removal and not a jq crash.
        old = self._pages(ok=300) + [
            {"id": "n", "url": 42, "fetch_status": "ok"},
            {"id": "e", "url": "", "fetch_status": "ok"},
        ]
        new = self._pages(ok=300) + [{"id": "n", "url": 42, "fetch_status": "ok"}]
        r = self._run(project_root, tmp_path, old, new)
        assert r.returncode == 0, r.stdout + r.stderr
        assert "Previously-live pages removed: 0 of 300" in r.stdout

    @pytest.mark.integration
    def test_step_fails_closed_on_non_object_page_entry_at_head(self, project_root, tmp_path):
        import json
        head = json.dumps({"schema_version": 2, "pages": self._pages(ok=300) + [None]})
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), old_raw=head)
        assert r.returncode != 0, r.stdout + r.stderr
        assert "not a valid JSON object" in r.stdout

    @pytest.mark.integration
    @pytest.mark.parametrize("head_text", ["[]", "null", '"str"', "42", "{} {}"])
    def test_step_fails_closed_on_non_object_head_manifest(self, project_root, tmp_path, head_text):
        # load_manifest() rejects any top level that is not one dict; so must the mirror.
        r = self._run(project_root, tmp_path, [], self._pages(ok=300), old_raw=head_text)
        assert r.returncode != 0, r.stdout + r.stderr
        assert "not a valid JSON object" in r.stdout


class TestWorkflowOutputs:
    """Test workflow outputs and artifacts."""

    @pytest.mark.integration
    def test_committed_data_files_exist(self, project_root):
        """v2 workflow output is the committed manifest + prose-free index (docs/ is gone)."""
        assert (project_root / "paths_manifest.json").is_file()
        assert (project_root / "search_index.json").is_file()
