# tool: binary_to_hex
# description: Converts a binary string to hexadecimal.
# author: @1998LJ
# example: binary_to_hex("1111") returns "F"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        dec = int(val, 2)
    except ValueError:
        return "Error: Argument must be a valid binary string."

    return hex(dec)[2:].upper()
