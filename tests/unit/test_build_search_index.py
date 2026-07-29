"""v2 search-index unit tests: schema, headings, stemmed terms, forbidden-field absence."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import build_search_index as bsi

SAMPLE_MD = """# Hooks

Hooks let you run commands. Matchers match tools. Settings configure hooks.

## Configuration

Configure your hooks with matchers.

### Advanced Matchers

```python
# this comment and def function() must NOT be indexed
def hook(): pass
```

- Use `PreToolUse` for pre-hooks
- See [the settings page](https://example.com/settings) for details
"""

ENTRY = {
    "id": "claude-code/hooks",
    "filename": "claude-code__hooks.md",
    "url": "https://code.claude.com/docs/en/hooks",
    "title": "Hooks",
    "category": "claude_code",
}

ALLOWED_KEYS = {"filename", "id", "title", "category", "url", "headings", "terms", "word_count"}
FORBIDDEN_KEYS = {"content_preview", "preview", "file_path", "keywords", "positions", "ngrams"}


class TestStem:
    def test_contract(self):
        assert bsi.stem("hooks") == "hook"
        assert bsi.stem("matchers") == "matcher"
        assert bsi.stem("running") == "runn"
        assert bsi.stem("uses") == "use"
        assert bsi.stem("classes") == "class"
        assert bsi.stem("used") == "used"      # <3 chars would remain -> unchanged
        assert bsi.stem("es") == "es"          # too short to strip


class TestSlugify:
    def test_github_style(self):
        assert bsi.slugify("Advanced Matchers") == "advanced-matchers"
        assert bsi.slugify("Use `PreToolUse` Hooks!") == "use-pretooluse-hooks"


class TestHeadings:
    def test_extracts_text_and_level_no_anchor(self):
        headings = bsi.extract_headings(SAMPLE_MD)
        texts = [h["text"] for h in headings]
        assert "Hooks" in texts
        assert "Configuration" in texts
        assert "Advanced Matchers" in texts
        cfg = next(h for h in headings if h["text"] == "Configuration")
        assert cfg["level"] == 2
        assert set(cfg.keys()) == {"text", "level"}  # anchor dropped (recomputable via slugify)

    def test_ignores_headings_inside_code_blocks(self):
        headings = bsi.extract_headings(SAMPLE_MD)
        # "# this comment ..." is inside a fenced block and must not appear.
        assert all("this comment" not in h["text"] for h in headings)


class TestTerms:
    def test_stemmed_bag_of_counts(self):
        terms = bsi.extract_terms(SAMPLE_MD)
        # 'hooks' and 'hook' both stem to 'hook' -> merged count.
        assert "hook" in terms
        assert terms["hook"] >= 2
        assert isinstance(terms["hook"], int)

    def test_stopwords_removed(self):
        terms = bsi.extract_terms("the and with for you your this that have")
        assert terms == {}

    def test_code_not_indexed(self):
        terms = bsi.extract_terms(SAMPLE_MD)
        # 'def' / 'pass' live only in the fenced code block.
        assert "def" not in terms
        assert "pass" not in terms

    def test_cap_enforced(self):
        big = " ".join(f"word{i}" for i in range(200))
        terms = bsi.extract_terms(big, cap=10)
        assert len(terms) <= 10


class TestIndexPageSchema:
    def test_only_allowed_keys(self):
        page = bsi.index_page(ENTRY, SAMPLE_MD)
        assert set(page.keys()) == ALLOWED_KEYS
        assert not (set(page.keys()) & FORBIDDEN_KEYS)

    def test_missing_content_still_indexed_by_title(self):
        page = bsi.index_page(ENTRY, "")
        assert page["title"] == "Hooks"
        assert page["headings"] == []
        assert page["terms"] == {}
        assert page["word_count"] == 0


class TestBuildIndex:
    def test_build_and_save_roundtrip(self, tmp_path):
        scratch = tmp_path / "scratch"
        scratch.mkdir()
        (scratch / "claude-code__hooks.md").write_text(SAMPLE_MD)
        manifest = {"pages": [ENTRY]}

        index = bsi.build_index(manifest, scratch)
        assert index["schema_version"] == 2
        assert len(index["pages"]) == 1

        out = tmp_path / "search_index.json"
        bsi.save_index(index, out)
        reloaded = json.loads(out.read_text())
        assert reloaded["pages"][0]["filename"] == "claude-code__hooks.md"
        # Whole-index forbidden-field sweep.
        for p in reloaded["pages"]:
            assert not (set(p.keys()) & FORBIDDEN_KEYS)
