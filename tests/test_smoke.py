from __future__ import annotations

from typer.testing import CliRunner

from hl_archive import __version__
from hl_archive.cli import app


def test_version_constant() -> None:
    assert __version__ == "0.1.0"


def test_cli_version_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_cli_help_lists_commands() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "fetch" in result.stdout
    assert "version" in result.stdout
