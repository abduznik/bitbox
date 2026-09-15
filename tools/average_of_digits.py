# tool: average_of_digits
# description: Computes the average of digits in an integer.
# author: @1998LJ
# example: average_of_digits("1234") returns "2.5"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "Error: Argument cannot be empty."

    digits = val[1:] if val.startswith('-') else val
    if not digits.isdigit():
        return "Error: Argument must be an integer."

    avg = sum(int(d) for d in digits) / len(digits)
    return f"{avg:g}"
