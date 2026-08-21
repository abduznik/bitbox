# tool: extract_digits
# description: Extract only digits from a string
# author: @isaakchoi
# example: extract_digits "a1b2c3" -> "123"

def run(*args) -> str:

    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]

    return "".join(filter(str.isdigit, text))
