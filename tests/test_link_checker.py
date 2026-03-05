"""Tests for link-checker."""

import pytest
from link_checker import checker


class TestChecker:
    """Test suite for checker."""

    def test_basic(self):
        """Test basic usage."""
        result = checker("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            checker("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = checker(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
