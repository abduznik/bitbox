# tool: is_automorphic
# description: Checks if a number is automorphic (its square ends with itself)
# author: @HarshRajSinghania
# example: is_automorphic "25" -> "True"

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    try:
        n = int(val)
    except ValueError:
        return "Error: Argument must be an integer."

    if n < 0:
        return "Error: Argument must be a non-negative integer."

    square = n * n
    return str(str(square).endswith(str(n)))
