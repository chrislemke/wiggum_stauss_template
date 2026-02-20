"""Tests for the main module."""

import pytest

from project_name.main import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that main() prints the expected greeting."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from project_name!\n"
