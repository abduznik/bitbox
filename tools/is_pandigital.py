# tool: is_pandigital
# description: Check if a string uses each digit 1-n exactly once.
# author: @CRYPTONIKAV
# example: is_pandigital "52134" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = str(args[0]).strip()
    if not text or not text.isdigit():
        return "False"
    digits = sorted(text)
    return str(digits == [str(d) for d in range(1, len(text) + 1)])
