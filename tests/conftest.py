"""Pytest configuration and fixtures. Markers are declared in pyproject.toml."""

import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Get project root directory."""
    return Path(__file__).parent.parent
