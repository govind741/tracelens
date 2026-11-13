# TraceLens

A self-hosted observability and evaluation dashboard for LLM apps.

TraceLens records the prompts and responses your app sends to language models,
tracks cost, latency and errors, and lets you score outputs to catch regressions.

## Status

Early development. Planned for the first milestone:

- [ ] Trace ingestion API (FastAPI + SQLite)
- [ ] Cost estimation from token counts
- [ ] Stats endpoints (summary, time series, per-model breakdown)
- [ ] Web dashboard with charts and a trace viewer
- [ ] Python SDK for sending traces
- [ ] Demo data generator

## Stack

Python 3.9+, FastAPI, SQLite, vanilla JS dashboard.

## License

MIT. See [LICENSE](LICENSE).
