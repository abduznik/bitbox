import sys
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).parent
AMMO_FILE = SCRIPT_DIR / "ammunition.yml"
QUEUE_FILE = SCRIPT_DIR / "queue.yml"


def load_yaml(path):
    if not path.exists():
        print(f"Error: {path} not found.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def main():
    count = 10

    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--count" and i < len(sys.argv) - 1:
            try:
                count = int(sys.argv[i + 1])
            except ValueError:
                print("Error: --count must be an integer.")
                sys.exit(1)

    ammo = load_yaml(AMMO_FILE)
    queue = load_yaml(QUEUE_FILE)

    unfired = []
    for category in ammo.values():
        if isinstance(category, list):
            for issue in category:
                if not issue.get("fired", False):
                    unfired.append(issue)

    if not unfired:
        print("No unfired rounds remaining in ammunition.")
        sys.exit(0)

    to_load = unfired[:count]

    for issue in to_load:
        issue["fired"] = True
        queue["rounds"].append({
            "title": issue["title"],
            "description": issue["description"],
            "signature": issue["signature"],
            "example": issue["example"],
            "labels": issue["labels"],
            "status": "pending",
        })

    queue["stats"]["total_loaded"] = queue["stats"].get("total_loaded", 0) + len(to_load)

    save_yaml(AMMO_FILE, ammo)
    save_yaml(QUEUE_FILE, queue)

    remaining = len(unfired) - len(to_load)
    print(f"Loaded {len(to_load)} rounds into queue. {remaining} rounds remaining in ammunition.")


if __name__ == "__main__":
    main()
