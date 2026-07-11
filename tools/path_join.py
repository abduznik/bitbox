# tool: path_join
# description: Joins multiple path segments into one normalized path
# author: @isaac-sun
# example: path_join "/home/user" "docs" "file.txt" → "/home/user/docs/file.txt"

import os
from pathlib import PurePosixPath, PureWindowsPath


def run(*args) -> str:
    if not args:
        raise ValueError("path_join requires at least one path segment")
    parts = [str(a) for a in args]
    if os.name == "nt":
        joined = PureWindowsPath(parts[0])
        for part in parts[1:]:
            joined = joined.joinpath(part)
        return str(joined)
    joined = PurePosixPath(parts[0])
    for part in parts[1:]:
        joined = joined.joinpath(part)
    return str(joined)
