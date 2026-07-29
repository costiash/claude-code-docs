"""Guard the stemming contract: Python (index build) and jq (query) must agree.

If these drift, search degrades silently — a query term stemmed one way in the
index and another way at query time simply stops matching. This runs both
implementations over a fixed word list and asserts equality.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
import build_search_index as bsi

pytestmark = pytest.mark.skipif(not shutil.which("jq"), reason="requires jq")

# This jq program MUST match the `def stem` in
# plugin/skills/claude-docs/scripts/content-search.sh exactly.
JQ_STEM = r'''
def stem:
  ascii_downcase as $w
  | if   ($w|endswith("ing")) and (($w|length) >= 6) then $w[0:-3]
    elif ($w|endswith("ed"))  and (($w|length) >= 5) then $w[0:-2]
    elif ($w|endswith("es"))  and (($w|length) >= 5) then $w[0:-2]
    elif ($w|endswith("s"))   and (($w|length) >= 4) then $w[0:-1]
    else $w end;
.[] | stem
'''

WORDS = [
    "hooks", "matcher", "matchers", "running", "uses", "used", "classes", "class",
    "es", "settings", "streaming", "messages", "agents", "sub", "mcp", "caching",
    "thinking", "batch", "processing", "images", "styles", "commands", "tools",
    "servers", "webhooks", "process", "sessions", "s", "a", "the", "index",
    "indexes", "boxes", "watched", "played", "sing", "ring", "bed", "bes",
]


def jq_stem_all(words):
    payload = "[" + ",".join(f'"{w}"' for w in words) + "]"
    out = subprocess.run(
        ["jq", "-r", JQ_STEM], input=payload, capture_output=True, text=True, check=True
    )
    return out.stdout.split("\n")[: len(words)]


def test_python_and_jq_stem_agree():
    py = [bsi.stem(w) for w in WORDS]
    jq = jq_stem_all(WORDS)
    mismatches = [(w, p, j) for w, p, j in zip(WORDS, py, jq) if p != j]
    assert not mismatches, f"stem parity broken: {mismatches}"
