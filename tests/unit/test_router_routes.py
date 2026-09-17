"""Help block <-> routing parity for the /docs router (plugin/skills/docs/SKILL.md).

Every form advertised in the help block must have a route, and every route
must be advertised, so help and behaviour cannot drift apart.
"""

import re
from pathlib import Path

ROUTER = Path(__file__).parent.parent.parent / "plugin" / "skills" / "docs" / "SKILL.md"

HELP_LINE = re.compile(r"^> `/docs ([^`]*)`")
ROUTE_LINE = re.compile(r"^\*\*(.+?)\*\* \((.*)\):$")
NONCANONICAL_ROUTE = re.compile(r"^\s*(?:[-*+]\s+)?(?:\*\*|__)\S.*\(.*\):\s*$")
# Placeholder forms in the help block that the catch-all route serves.
PLACEHOLDERS = {"<topic>", "<question>"}


def _first_token(form: str) -> str:
    return form.split()[0]


def parse():
    text = ROUTER.read_text()
    routing = text.split("## Routing", 1)[1].split("\n## ", 1)[0]
    # The help block is the usage text of the "No arguments / help" route and
    # must live in that paragraph only: usage lines anywhere else (say, under
    # the catch-all route) would print on every lookup.
    paragraphs = routing.split("\n\n")
    help_par = next((p for p in paragraphs if p.startswith("**No arguments / help**")), "")
    assert help_par, "no 'No arguments / help' route paragraph"
    help_forms = [m.group(1) for m in (HELP_LINE.match(l) for l in help_par.splitlines()) if m]
    total = sum(1 for l in text.splitlines() if HELP_LINE.match(l))
    assert total == len(help_forms), f"{total - len(help_forms)} usage line(s) outside the help route"
    routes = {}
    for line in routing.splitlines():
        # Routes are bold headers only; a sub-heading in this section would be
        # a route the parity checks cannot see, so it is rejected outright.
        assert not re.match(r"^#{3,} ", line), f"unexpected heading in Routing: {line!r}"
        # A route-shaped line that is not a canonical column-0 `**Name** (…):`
        # header (list marker, indentation, __underscore__ bold) would be
        # skipped silently; reject it instead.
        assert not (NONCANONICAL_ROUTE.match(line) and not line.startswith("**")), (
            f"route header not in canonical position/shape: {line!r}"
        )
        if not line.startswith("**"):
            continue
        m = ROUTE_LINE.match(line)
        # Every bold line in the Routing section is a route header; one that
        # does not fit the `**Name** (`trigger`, ...):` shape would otherwise be
        # invisible to both parity checks.
        assert m, f"route header not in the expected shape: {line!r}"
        assert m.group(1) not in routes, f"duplicate route header: {m.group(1)!r}"
        routes[m.group(1)] = re.findall(r"`([^`]+)`", m.group(2))
    return help_forms, routes


def test_router_has_help_and_routes():
    help_forms, routes = parse()
    assert len(help_forms) >= 7
    assert "No arguments / help" in routes and "Everything else" in routes


def test_no_trigger_token_is_claimed_by_two_routes():
    """Two routes answering to the same first word would be ambiguous."""
    _, routes = parse()
    owners = {}
    for name, triggers in routes.items():
        for tok in {_first_token(t) for t in triggers}:
            assert tok not in owners, f"trigger {tok!r} claimed by {owners[tok]!r} and {name!r}"
            owners[tok] = name


def test_every_help_form_is_routed():
    help_forms, routes = parse()
    trigger_tokens = {_first_token(t) for ts in routes.values() for t in ts}
    for form in help_forms:
        tok = _first_token(form)
        if tok in PLACEHOLDERS:
            continue  # served by the catch-all route
        assert tok in trigger_tokens, f"help advertises `/docs {form}` but no route triggers on {tok!r}"


def test_every_route_is_advertised():
    help_forms, routes = parse()
    help_tokens = {_first_token(f) for f in help_forms}
    for name, triggers in routes.items():
        if name in ("No arguments / help", "Everything else"):
            continue
        assert any(_first_token(t) in help_tokens for t in triggers), (
            f"route {name!r} ({triggers}) is not listed in the help block"
        )
