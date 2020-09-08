#! /usr/bin/env python3
import subprocess
from pathlib import Path
import shutil


def main() -> None:
    # Load user list
    with open("users.txt") as f:
        users = f.read().split("\n")

    root = Path("git-spoofing")
    if root.exists:
        shutil.rmtree(root)
    root.mkdir()

    subprocess.check_call(["git", "init"], cwd=root)

    file = root / "text.txt"

    for user in users:
        with open(file, "a") as f:
            f.write(user + "\n")

        subprocess.check_call(["git", "add", file.relative_to(root)], cwd=root)
        subprocess.check_call(["git", "config", "--local", "user.email", f"{user}@users.noreply.github.com "], cwd=root)
        subprocess.check_call(["git", "config", "--local", "user.name", user], cwd=root)
        subprocess.check_call(["git", "commit", "-m", user], cwd=root)


if __name__ == "__main__":
    main()
