# tool: path_parent
# description: returns the parent directory of a path
# author: @Solaris-star
# example: path_parent "/tmp/foo/bar.txt" -> "/tmp/foo"

from pathlib import PurePosixPath


def run(*args) -> str:
    if not args:
        return "Error: expected a path argument"
    return str(PurePosixPath(args[0]).parent)

