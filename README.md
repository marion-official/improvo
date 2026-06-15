# Improvo

Improvo is a game where you are given a scenario and a cast of characters. You collaborate with the AI to build the narrative together.

## Installation

**Prerequisites:**
- Python 3.9+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- An [Anthropic API key](https://console.anthropic.com/)

```bash
git clone https://github.com/your-username/improvo.git
cd improvo
uv sync
```

Copy the environment file and set your Anthropic API key:

```bash
cp .env.example .env
# edit .env and set ANTHROPIC_API_KEY=your-key-here
```

## Running

```bash
uv run main.py
```

## Rules
1. You can perform actions by writing them surrounded by double asterisks. For example, **walks to the door**.
2. You can talk to other characters by writing their name followed by a colon and then what you want to say. For example, "Alice: Hello, how are you, my dear?".
3. You can ask the AI to describe the scene or the characters by writing "Describe: " followed by what you want described. For example, "Describe: The room".

## Future improvements

- Scene control: a way to end or reset the current scene, e.g. `New scene:` or `Reset:`.
- Mid-story character introduction: a way to add new characters during play.
- Out-of-character mode: a way to speak to the AI outside the story, e.g. `(( ... ))`, for meta instructions or questions.


