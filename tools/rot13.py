# tool: rot13
# description: Applies the ROT13 cipher to a string.
# author: @1998LJ
# example: rot13 "hello" -> "uryyb"

import codecs


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return codecs.encode(str(args[0]), "rot_13")
