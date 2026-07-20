# tool: percentage
# description: computes percentage: part/whole * 100
# author: @Solaris-star
# example: percentage "25" "200" -> "12.5"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected part and whole"
    try:
        part = float(args[0])
        whole = float(args[1])
    except ValueError:
        return "Error: arguments must be numbers"
    if whole == 0:
        return "Error: whole must not be zero"
    value = (part / whole) * 100
    if value.is_integer():
        return str(int(value))
    return str(value)
