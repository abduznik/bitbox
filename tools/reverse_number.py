# tool: reverse_number
# description: Reverses the digits of an integer.
# author: @1998LJ
# example: reverse_number("1234") returns "4321"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    is_negative = val.startswith('-')
    digits = val[1:] if is_negative else val

    if not digits.isdigit():
        return "Error: Argument must be an integer."

    reversed_digits = digits[::-1].lstrip('0')
    if not reversed_digits:
        return "0"

    result = f"-{reversed_digits}" if is_negative else reversed_digits
    return result
