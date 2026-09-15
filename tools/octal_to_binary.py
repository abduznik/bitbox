# tool: octal_to_binary
# description: Converts an octal string to binary.
# author: @1998LJ
# example: octal_to_binary("12") returns "1010"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        dec = int(val, 8)
    except ValueError:
        return "Error: Argument must be a valid octal string."

    return bin(dec)[2:]
