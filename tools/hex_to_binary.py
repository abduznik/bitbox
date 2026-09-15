# tool: hex_to_binary
# description: Converts a hexadecimal string to binary.
# author: @1998LJ
# example: hex_to_binary("A") returns "1010"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        dec = int(val, 16)
    except ValueError:
        return "Error: Argument must be a valid hexadecimal string."

    return bin(dec)[2:]
