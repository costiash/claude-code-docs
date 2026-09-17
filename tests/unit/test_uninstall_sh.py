"""Contract tests for uninstall.sh (offline, non-interactive stdin).

The script never deletes anything without a terminal, so these runs are safe:
they only check what the closing lines claim happened.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

UNINSTALL = Path(__file__).parent.parent.parent / "uninstall.sh"

pytestmark = pytest.mark.skipif(not shutil.which("bash"), reason="requires bash")


def run(home: Path):
    return subprocess.run(
        ["bash", str(UNINSTALL)],
        env={"HOME": str(home), "PATH": "/usr/bin:/bin"},
        stdin=subprocess.DEVNULL,  # not a tty: the script must not prompt
        capture_output=True,
        text=True,
        timeout=30,
    )


class TestClosingLine:
    def test_kept_docs_noninteractive_is_named_not_completed(self, tmp_path):
        home = tmp_path / "home"
        docs = home / ".claude-code-docs"
        docs.mkdir(parents=True)
        (docs / "paths_manifest.json").write_text("{}")
        r = run(home)
        assert r.returncode == 0, r.stderr
        lines = r.stdout.splitlines()
        assert f"Plugin uninstall instructions printed; local docs kept at {docs}" in lines
        # The manual-removal hint must be copy-paste safe for any path.
        quoted = subprocess.run(
            ["bash", "-c", 'printf %q "$1"', "_", str(docs)], capture_output=True, text=True
        ).stdout
        assert f"Run interactively to remove, or: rm -rf {quoted}" in lines
        assert "Uninstall complete." not in lines
        assert lines[-1].startswith("To reinstall:")
        assert docs.is_dir() and (docs / "paths_manifest.json").exists()

    def test_hint_is_paste_safe_with_awkward_home(self, tmp_path):
        home = tmp_path / 'we"ird home'
        docs = home / ".claude-code-docs"
        docs.mkdir(parents=True)
        r = run(home)
        assert r.returncode == 0, r.stderr
        hint = next(l for l in r.stdout.splitlines() if l.startswith("Run interactively"))
        quoted = hint.split("rm -rf ", 1)[1]
        # Round-trip the quoted form through bash: it must name the same path.
        back = subprocess.run(
            ["bash", "-c", f"printf %s {quoted}"], capture_output=True, text=True
        ).stdout
        assert back == str(docs)

    def test_nothing_to_keep_reports_complete(self, tmp_path):
        home = tmp_path / "home"
        home.mkdir()
        r = run(home)
        assert r.returncode == 0, r.stderr
        lines = r.stdout.splitlines()
        assert "Uninstall complete." in lines
        assert not any(line.startswith("Plugin uninstall instructions printed") for line in lines)
        assert lines[-1].startswith("To reinstall:")
