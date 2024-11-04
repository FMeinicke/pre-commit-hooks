from __future__ import annotations

import argparse
import os
import subprocess
import sys
from typing import Sequence


def check_no_special_commits(prefixes: Sequence[str] | None = None) -> int:
    """
    Checks that no commit starts with a special string that would indicate that
    the commit is a fixup, squash or amend commit. This is useful to prevent
    developers from pushing these commits to the remote repository.

    Parameters
    ----------
    prefixes : Sequence[str], optional
        A list of special strings that should be checked for. Default is
        ['squash! ', 'fixup! ', 'amend! ']

    Returns
    -------
    int
        0 if all commits are valid, 1 otherwise
    """

    if prefixes is None or not prefixes:
        prefixes = ["squash! ", "fixup! ", "amend! "]

    ret = 0

    # Get the list of commits to be pushed
    from_ref = os.environ.get("PRE_COMMIT_FROM_REF")
    to_ref = os.environ.get("PRE_COMMIT_TO_REF", "HEAD")
    commit_list = (
        subprocess.check_output(
            ["git", "rev-list", f"{from_ref}..{to_ref}" if from_ref else to_ref]
        )
        .decode()
        .splitlines()
    )

    # Check each commit message
    for commit in commit_list:
        commit_message = (
            subprocess.check_output(
                ["git", "log", "--format=%B", "-n", "1", commit]
            )
            .decode()
            .strip()
        )
        if any(commit_message.startswith(prefix) for prefix in prefixes):
            print(
                f"commit {commit} starts with a special string",
                file=sys.stderr,
            )
            ret = 1

    if ret == 0:
        print("No special commits found")
    return ret


def main(argv: Sequence[str] | None = None) -> int:  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prefix",
        nargs="*",
        help="Special strings that should be checked for",
    )
    args = parser.parse_args(argv)

    return check_no_special_commits(args.prefix)


if __name__ == "__main__":
    raise SystemExit(main())
