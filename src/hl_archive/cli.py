from __future__ import annotations

import typer

from hl_archive import __version__

app = typer.Typer(
    name="hl-archive",
    help="Turn Hyperliquid S3 lz4 dumps into clean Parquet datasets.",
    no_args_is_help=True,
    add_completion=False,
)


@app.command()
def version() -> None:
    """Print the installed hl-archive version."""
    typer.echo(__version__)


@app.command()
def fetch(
    market: str = typer.Argument(..., help="Market symbol, e.g. BTC."),
    start: str = typer.Option(..., "--start", help="Start date (YYYY-MM-DD)."),
    end: str = typer.Option(..., "--end", help="End date (YYYY-MM-DD)."),
    out: str = typer.Option("./data", "--out", help="Output directory for Parquet files."),
) -> None:
    """Download and decode Hyperliquid S3 dumps into Parquet. (Not implemented yet.)"""
    raise NotImplementedError("fetch is the next milestone — see README roadmap.")


if __name__ == "__main__":
    app()
