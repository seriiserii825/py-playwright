# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management with Python 3.12.

```bash
uv sync                          # install dependencies
uv run playwright install        # install Playwright browsers (required first time)
```

## Running

```bash
uv run python main.py            # run the main script
```

## Linting & Type Checking

```bash
uv run flake8 .                  # lint
uv run mypy .                    # type check
uv run autopep8 --in-place .     # auto-format
```

## Architecture

`main.py` is the entry point; it calls functions from `modules/`. Each module encapsulates a distinct Playwright usage pattern:

- `modules/sync_playwright_api.py` — synchronous Playwright browser automation (launches Chromium, navigates, screenshots)

New automation scripts should be added as functions in appropriately named modules under `modules/`, then imported and called from `main()`.

Playwright is run in **non-headless mode** (`headless=False`) by default. Change to `headless=True` for CI or background runs.
