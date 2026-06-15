from dotenv import load_dotenv
load_dotenv()

import yaml
from pathlib import Path
from anthropic import Anthropic


def load_content():
    path = Path(__file__).parent / "content.yml"
    with open(path) as f:
        return yaml.safe_load(f)


def format_scenario(scenario):
    lines = [f"Scenario: {scenario['description']}", "Characters:"]
    for character in scenario["characters"]:
        lines.append(f"- {character['name']}: {character['description']}")
    return "\n".join(lines)


def pick_scenario(scenarios):
    print("Choose a scenario:\n")
    for i, scenario in enumerate(scenarios, 1):
        print(f"  {i}. {scenario['name']}")
    print()
    while True:
        choice = input("Enter a number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(scenarios):
            return scenarios[int(choice) - 1]
        print(f"Please enter a number between 1 and {len(scenarios)}.")


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(client, model, messages, system):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        system=system,
        messages=messages,
    )
    return message.content[0].text


if __name__ == '__main__':
    client = Anthropic()
    model = "claude-haiku-4-5-20251001"

    content = load_content()
    rules_user = content["rules_user"]
    rules_game = content["rules_game"]
    scenarios = content["scenarios"]

    print(rules_user)

    scenario = pick_scenario(scenarios)
    system = rules_game + "\n" + format_scenario(scenario)

    print(f"\n--- {scenario['name']} ---\n")
    print(scenario["description"])
    print("Characters:")
    for character in scenario["characters"]:
        print(f"{character['name']}: {character['description']}")
    print("\nStart your adventure! Type your actions, dialogue, or requests for descriptions. CTRL+C to exit.\n")

    messages = []

    while True:
        user_input = input(":> ").strip()
        if not user_input:
            continue

        add_user_message(messages, user_input)
        response = chat(client, model, messages, system)
        print(f"\n{response}\n")
        add_assistant_message(messages, response)
