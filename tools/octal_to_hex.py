# tool: octal_to_hex
# description: Converts an octal number to hexadecimal.
# author: @1998LJ
# example: octal_to_hex("17") returns "F"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        dec = int(val, 8)
    except ValueError:
        return "Error: Argument must be a valid octal number."

    return hex(dec)[2:].upper()
