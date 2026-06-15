# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv sync          # install dependencies
uv run main.py   # run the game
```

## Architecture

This is a single-file CLI application. All game logic lives in `main.py`; all content (rules and scenarios) lives in `content.yml`.

**`main.py`** — entry point and game loop:
- Loads `content.yml` at startup via `load_content()`
- Presents a scenario picker to the player via `pick_scenario()`
- Builds the system prompt by concatenating `rules_game` + the selected scenario (via `format_scenario()`)
- Runs a `while True` input loop, maintaining a `messages` list for the full conversation history
- Calls `client.messages.create()` on every turn, passing the full history and system prompt

**`content.yml`** — single source of truth for all text content:
- `rules_user`: printed to the player at startup
- `rules_game`: passed as the `system` parameter to the Claude API
- `scenarios`: list of playable scenarios, each with a `name`, `description`, and `characters` list

The system prompt sent to Claude is `rules_game + formatted scenario`, where `format_scenario()` renders the scenario description and character list into plain text.

## Model

Currently using `claude-haiku-4-5-20251001`. The `system` parameter is passed as a top-level field in `client.messages.create()`, not as a role in the messages array (mid-conversation system role requires Opus 4.8).
