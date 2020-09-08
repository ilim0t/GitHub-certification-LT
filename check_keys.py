#! /usr/bin/env python3
import re
import subprocess
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Set


def main() -> None:
    # Load user list
    with open("users.txt") as f:
        users = f.read().split("\n")

    # Download keys
    keys_dir = Path("keys")
    keys_dir.mkdir(exist_ok=True)

    for user_name in users:
        output_path = keys_dir / f"{user_name}.keys"
        if not output_path.exists():
            urllib.request.urlretrieve(f"https://github.com/{user_name}.keys", output_path)

    # Check algorithm
    algorithm_list: DefaultDict[str, Set[str]] = defaultdict(set)
    for idx, user_name in enumerate(users):
        if idx:
            print()
        print(user_name + ":")

        try:
            res = subprocess.check_output(["ssh-keygen", "-l", "-f", keys_dir / f"{user_name}.keys"])
        except subprocess.CalledProcessError:
            continue

        for line in res.decode("utf-8").split("\n"):
            match = re.search(r"\((.+)\)", line)
            if match is None:
                continue

            algorithm, bit_size = match[1], line.split(" ", 1)[0]
            print(algorithm, bit_size)
            algorithm_list[user_name].add(f"{algorithm} {bit_size}")

    # Show algorithm
    print()
    for user, algorithms in algorithm_list.items():
        print(user + ":")
        for algorithm in algorithms:
            print(f"\t{algorithm}")


if __name__ == "__main__":
    main()
