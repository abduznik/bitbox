# tool: path_normalize
# description: normalizes a filesystem path (collapse . and .., normalize separators)
# author: @Solaris-star
# example: path_normalize "a/b/../c" -> "a/c"

import posixpath


def run(*args) -> str:
    if not args:
        return "Error: expected a path argument"
    return posixpath.normpath(args[0].replace("\\", "/"))
