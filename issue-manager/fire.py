import sys
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).parent
QUEUE_FILE = SCRIPT_DIR / "queue.yml"


def load_queue():
    if not QUEUE_FILE.exists():
        print(f"Error: {QUEUE_FILE} not found. Run reload.py first.")
        sys.exit(1)
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_queue(data):
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def create_issue(title, body, labels):
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    for label in labels:
        cmd.extend(["--label", label])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Error creating issue: {result.stderr.strip()}")
        return None
    return result.stdout.strip()


def format_body(round_data):
    return (
        "## Tool Request\n\n"
        f"**Description:** {round_data['description']}\n\n"
        "**Signature**\n"
        "```python\n"
        f"{round_data['signature']}\n"
        "```\n\n"
        "**Example**\n"
        f"`{round_data['example']}`\n\n"
        "---\n"
        "_This issue was auto-generated. Pick it up by commenting below!_"
    )


def main():
    count = 5
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg == "--count":
            continue
        elif sys.argv[sys.argv.index(arg) - 1] == "--count":
            try:
                count = int(arg)
            except ValueError:
                print("Error: --count must be an integer.")
                sys.exit(1)

    data = load_queue()
    pending = [r for r in data["rounds"] if r["status"] == "pending"]

    if not pending:
        print("Magazine empty. Run reload.py to refill.")
        sys.exit(0)

    to_fire = pending[:count]

    if dry_run:
        print(f"DRY RUN: would fire {len(to_fire)} issues\n")
        for r in to_fire:
            print(f"  - {r['title']}")
        sys.exit(0)

    fired_count = 0
    for r in to_fire:
        body = format_body(r)
        print(f"Firing: {r['title']}")
        url = create_issue(r["title"], body, r["labels"])
        if url:
            print(f"  -> {url}")
            r["status"] = "spent"
            fired_count += 1
        else:
            print(f"  -> FAILED")
        time.sleep(2)

    data["stats"]["total_fired"] = data["stats"].get("total_fired", 0) + fired_count
    data["stats"]["last_fired"] = datetime.now(timezone.utc).isoformat()

    save_queue(data)
    print(f"\nFired {fired_count} issues.")


if __name__ == "__main__":
    main()
