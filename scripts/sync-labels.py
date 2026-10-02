#!/usr/bin/env python3
"""Idempotently create/update shared GitHub labels.

GitHub's default labels are intentionally left untouched.
Requires the GitHub CLI (gh) to be installed and authenticated.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def gh(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        text=True,
        capture_output=True,
        check=False,
    )


def load_labels(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"{path} must contain a JSON array")

    labels: list[dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict):
            raise SystemExit("each label entry must be an object")
        for key in ("name", "color", "description"):
            if not isinstance(item.get(key), str) or not item[key]:
                raise SystemExit(f"label entry is missing non-empty {key!r}: {item!r}")
        labels.append(item)
    return labels


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="Target repository in OWNER/REPO form.")
    parser.add_argument(
        "--labels",
        default=".github/labels.json",
        help="Path to shared label definition JSON.",
    )
    args = parser.parse_args()

    labels = load_labels(Path(args.labels))

    probe = gh("repo", "view", args.repo, "--json", "nameWithOwner", "--jq", ".nameWithOwner")
    if probe.returncode != 0:
        raise SystemExit(probe.stderr.strip() or f"cannot access {args.repo}")

    for label in labels:
        name = label["name"]
        color = label["color"].lstrip("#")
        description = label["description"]
        encoded_name = name.replace(":", "%3A")

        check = gh("api", f"repos/{args.repo}/labels/{encoded_name}", "--silent")

        if check.returncode == 0:
            action = "update"
            result = gh(
                "api",
                "--method",
                "PATCH",
                f"repos/{args.repo}/labels/{encoded_name}",
                "-f",
                f"new_name={name}",
                "-f",
                f"color={color}",
                "-f",
                f"description={description}",
                "--silent",
            )
        else:
            action = "create"
            result = gh(
                "api",
                "--method",
                "POST",
                f"repos/{args.repo}/labels",
                "-f",
                f"name={name}",
                "-f",
                f"color={color}",
                "-f",
                f"description={description}",
                "--silent",
            )

        if result.returncode != 0:
            print(f"ERROR {action} {name}: {result.stderr.strip()}")
            return 1

        print(f"{action}: {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
