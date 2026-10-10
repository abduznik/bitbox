# tool: is_automorphic
# description: Check if a number is automorphic.
# author: @CRYPTONIKAV
# example: is_automorphic "25" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    try:
        n = int(val)
    except ValueError:
        return f"Error: Invalid integer '{val}'."
    if n < 0:
        return "Error: Expected a non-negative integer."

    return str(str(n * n).endswith(str(n)))
