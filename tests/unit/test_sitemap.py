"""Sitemap parsing/discovery tests: XXE rejection, namespace handling, filtering (offline)."""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetcher.sitemap import _parse_xml_safely, discover_sitemap_entries

NAMESPACED_SITEMAP = b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://code.claude.com/docs/en/hooks</loc>
    <lastmod>2026-07-16T00:00:00Z</lastmod>
  </url>
  <url>
    <loc>https://code.claude.com/docs/en/mcp</loc>
  </url>
  <url>
    <loc>https://code.claude.com/docs/de/hooks</loc>
    <lastmod>2026-07-16T00:00:00Z</lastmod>
  </url>
  <url>
    <loc>https://code.claude.com/docs/en/examples/demo</loc>
  </url>
</urlset>"""

PLAIN_SITEMAP = b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset>
  <url><loc>https://platform.claude.com/docs/en/api/messages</loc></url>
</urlset>"""

BILLION_LAUGHS = b"""<?xml version="1.0"?>
<!DOCTYPE lolz [
  <!ENTITY lol "lol">
  <!ENTITY lol2 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
  <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://code.claude.com/docs/en/&lol3;</loc></url>
</urlset>"""


def _session_for(responses):
    """Map url -> (status, bytes); anything else raises ConnectionError."""
    session = MagicMock()

    def get(url, **kwargs):
        if url not in responses:
            raise requests.ConnectionError(f"no route to {url}")
        status, content = responses[url]
        resp = MagicMock()
        resp.status_code = status
        resp.content = content
        if status >= 400:
            resp.raise_for_status.side_effect = requests.HTTPError(f"{status}")
        else:
            resp.raise_for_status.return_value = None
        return resp

    session.get.side_effect = get
    return session


class TestParseXmlSafely:
    def test_rejects_billion_laughs_dtd(self):
        with pytest.raises(ValueError, match="DTD/ENTITY"):
            _parse_xml_safely(BILLION_LAUGHS)

    def test_rejects_doctype_case_insensitive(self):
        with pytest.raises(ValueError):
            _parse_xml_safely(b'<?xml version="1.0"?><!doctype foo><urlset/>')

    def test_rejects_external_entity(self):
        payload = (
            b'<?xml version="1.0"?><!DOCTYPE r [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>'
            b"<urlset><url><loc>&xxe;</loc></url></urlset>"
        )
        with pytest.raises(ValueError):
            _parse_xml_safely(payload)

    def test_parses_normal_namespaced_sitemap(self):
        root = _parse_xml_safely(NAMESPACED_SITEMAP)
        ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [e.text for e in root.findall(".//ns:loc", ns)]
        assert "https://code.claude.com/docs/en/hooks" in locs
        assert len(locs) == 4

    def test_parses_plain_sitemap(self):
        root = _parse_xml_safely(PLAIN_SITEMAP)
        assert root.find(".//loc").text == "https://platform.claude.com/docs/en/api/messages"


class TestDiscoverSitemapEntries:
    SITEMAP_URL = "https://code.claude.com/docs/sitemap.xml"

    def _discover(self, content):
        session = _session_for({self.SITEMAP_URL: (200, content)})
        return discover_sitemap_entries(session, urls=[self.SITEMAP_URL])

    def test_namespaced_sitemap_entries_extracted(self):
        entries = self._discover(NAMESPACED_SITEMAP)
        urls = [e["url"] for e in entries]
        assert "https://code.claude.com/docs/en/hooks" in urls
        assert "https://code.claude.com/docs/en/mcp" in urls
        assert urls == sorted(urls)

    def test_non_english_and_examples_filtered(self):
        entries = self._discover(NAMESPACED_SITEMAP)
        urls = [e["url"] for e in entries]
        assert all("/docs/de/" not in u for u in urls)
        assert all("/examples/" not in u for u in urls)
        assert len(urls) == 2  # hooks + mcp only

    def test_lastmod_extracted_and_none_when_absent(self):
        by_url = {e["url"]: e["lastmod"] for e in self._discover(NAMESPACED_SITEMAP)}
        assert by_url["https://code.claude.com/docs/en/hooks"] == "2026-07-16T00:00:00Z"
        assert by_url["https://code.claude.com/docs/en/mcp"] is None

    def test_plain_unnamespaced_sitemap_supported(self):
        session = _session_for({"https://platform.claude.com/sitemap.xml": (200, PLAIN_SITEMAP)})
        entries = discover_sitemap_entries(session, urls=["https://platform.claude.com/sitemap.xml"])
        assert entries == [
            {"url": "https://platform.claude.com/docs/en/api/messages", "lastmod": None}
        ]


class TestSitemapFailClosed:
    """A configured sitemap that errors or yields zero pages aborts the run."""

    GOOD = "https://code.claude.com/docs/sitemap.xml"
    BAD = "https://platform.claude.com/sitemap.xml"

    def test_http_error_aborts(self):
        session = _session_for({self.GOOD: (200, NAMESPACED_SITEMAP), self.BAD: (500, b"oops")})
        with pytest.raises(RuntimeError, match="Discovery source failed"):
            discover_sitemap_entries(session, urls=[self.GOOD, self.BAD])

    def test_network_error_aborts(self):
        session = _session_for({self.GOOD: (200, NAMESPACED_SITEMAP)})  # BAD unroutable
        with pytest.raises(RuntimeError, match="Discovery source failed"):
            discover_sitemap_entries(session, urls=[self.GOOD, self.BAD])

    def test_zero_english_pages_aborts(self):
        empty = b'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://code.claude.com/pricing</loc></url></urlset>'
        session = _session_for({self.GOOD: (200, empty)})
        with pytest.raises(RuntimeError, match="zero English"):
            discover_sitemap_entries(session, urls=[self.GOOD])

    def test_dtd_payload_aborts_run(self):
        session = _session_for({self.GOOD: (200, BILLION_LAUGHS)})
        with pytest.raises(RuntimeError, match="Discovery source failed"):
            discover_sitemap_entries(session, urls=[self.GOOD])
