# tool: rotate_string
# description: Rotate a string left by n characters
# author: @yuefdev
# example: rotate_string "abc" "1" -> "bca"


def run(*args) -> str:
    """Rotate characters left; negative counts rotate right."""
    if len(args) != 2:
        return "Error: expected text and rotation count"
    try:
        n = int(args[1])
    except ValueError:
        return "Error: rotation count must be an integer"
    text = args[0]
    if not text:
        return ""
    n %= len(text)
    return text[n:] + text[:n]
