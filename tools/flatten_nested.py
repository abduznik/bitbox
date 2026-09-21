# tool: flatten_nested
# description: Flattens a comma-separated list with one level of bracketed nesting.
# author: @1998LJ
# example: flatten_nested "1,[2,3],4" -> "1,2,3,4"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = str(args[0]).strip()
    if not text:
        return ""

    items = []
    token = []
    depth = 0

    for char in text:
        if char == "[":
            if depth == 1:
                return "Error: Only one level of nesting is supported."
            depth = 1
        elif char == "]":
            if depth == 0:
                return "Error: Unmatched closing bracket."
            depth = 0
        elif char == ",":
            value = "".join(token).strip()
            if value:
                items.append(value)
            token = []
        else:
            token.append(char)

    if depth != 0:
        return "Error: Unmatched opening bracket."

    value = "".join(token).strip()
    if value:
        items.append(value)

    return ",".join(items)
