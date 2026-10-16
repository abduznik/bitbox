# tool: pad_center
# description: Center a string to a width using a single padding character
# author: @Wkhanex
# example: pad_center "hi" "6" "-" -> "--hi--"


def run(*args) -> str:
    """Center without truncating; require a nonnegative width and one fill character."""
    if len(args) != 3:
        raise ValueError("expected text, width and one padding character")
    text, width, character = args
    width = int(width)
    if width < 0:
        raise ValueError("width must be nonnegative")
    if len(character) != 1:
        raise ValueError("padding must be exactly one character")
    return text.center(width, character)
