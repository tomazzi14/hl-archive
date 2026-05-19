# hl-archive

> Turn Hyperliquid's raw S3 `lz4` dumps into clean Parquet datasets — queryable with Polars or DuckDB in one line.

[![CI](https://github.com/CHANGE_ME/hl-archive/actions/workflows/ci.yml/badge.svg)](https://github.com/CHANGE_ME/hl-archive/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/hl-archive.svg)](https://pypi.org/project/hl-archive/)
[![Python](https://img.shields.io/pypi/pyversions/hl-archive.svg)](https://pypi.org/project/hl-archive/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

`hl-archive` is the data layer that the Hyperliquid Python ecosystem is missing. It downloads Hyperliquid's public S3 dumps, decodes the `lz4`-framed JSON, and writes partitioned Parquet that loads in milliseconds — so you can stop writing the same ingestion script for every research notebook.

It's the foundation under [hyperbt](https://github.com/CHANGE_ME/hyperbt) (funding-aware Python backtester), but it stands on its own.

## Why

Hyperliquid publishes raw market data to a public S3 bucket. The format is `.lz4`-framed line-delimited JSON, organized by market and hour. Today every algo trader on the ecosystem rolls their own loader — and the only existing alternative has 27 stars, 7 commits, and treats Hyperliquid as a flat data dump.

`hl-archive` does three things well:

- **Fetch** — pulls hourly dumps from the official `requester-pays` bucket with `boto3`, retries baked in.
- **Decode** — streams `lz4` frames, parses event records, normalizes schemas across market types.
- **Query** — writes partitioned Parquet (`market=BTC/year=2026/month=05/...`) that Polars and DuckDB read in milliseconds.

## Install

```bash
pip install hl-archive
# or, with uv:
uv add hl-archive
```

Requires Python 3.11+.

## Quickstart

```bash
# Download a week of BTC perp data
hl-archive fetch BTC --start 2026-05-01 --end 2026-05-07 --out ./data
```

```python
import polars as pl

df = pl.scan_parquet("data/market=BTC/**/*.parquet").collect()
print(df.head())
```

## CLI

```
hl-archive fetch <market> --start YYYY-MM-DD --end YYYY-MM-DD --out <dir>
hl-archive version
```

## Status & roadmap

This is **v0.1 — alpha**. The CLI surface is stable enough to start integrating into research notebooks, but expect breaking changes through v0.x.

- [x] Project scaffolding, CI, packaging
- [ ] S3 fetch with `requester-pays`
- [ ] `lz4` frame decoder
- [ ] Parquet writer (partitioned by market/date)
- [ ] Polars-native reader helper
- [ ] Schema normalization across perp / spot / book / fills
- [ ] Funding-rate replay helper (consumed by `hyperbt`)

## Caveats

- **Data freshness:** Hyperliquid's S3 archive refreshes roughly once a month with no SLA. For live or near-live data, use the official Hyperliquid WebSocket, not this archive.
- **Cost:** the S3 bucket is `requester-pays` — you pay AWS egress for what you pull. Single-market tests cost cents; multi-market historical pulls can run into single-digit dollars.
- **Schema drift:** Hyperliquid changes payload formats periodically. `hl-archive` pins to a known-good snapshot per release; check the changelog before upgrading.

## Related projects

- [hyperbt](https://github.com/CHANGE_ME/hyperbt) — Python backtester for Hyperliquid, funding-aware, built on `hl-archive`.
- [hl-tui](https://github.com/CHANGE_ME/hl-tui) — terminal dashboard for live Hyperliquid portfolios.
- [hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) — official Python SDK (live API + WebSocket).

## Contributing

Issues and PRs welcome. Please open an issue before starting work on a non-trivial change so we can align on scope.

```bash
git clone https://github.com/CHANGE_ME/hl-archive
cd hl-archive
uv sync
uv run pytest
uv run ruff check
```

## License

MIT — see [LICENSE](LICENSE).
