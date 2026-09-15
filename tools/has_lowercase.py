# tool: has_lowercase
# description: Checks if a string contains at least one lowercase character.
# author: @1998LJ
# example: has_lowercase("Hello") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0])
    return str(any(c.islower() for c in val))
