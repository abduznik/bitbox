# tool: leet_speak
# description: Replace common letters with their leet-speak digits
# author: @Wkhanex
# example: leet_speak "hello" -> "h3110"


def run(*args) -> str:
    """Map a/e/i/l/o/s/t in either case; preserve other characters."""
    if len(args) != 1:
        raise ValueError("expected one string")
    mapping = dict(zip("aeilost", "4311057"))
    mapping.update({letter.upper(): digit for letter, digit in list(mapping.items())})
    return args[0].translate(str.maketrans(mapping))
