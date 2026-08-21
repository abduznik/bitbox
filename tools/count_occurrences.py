# tool: count_occurrences
# description: Count occurrences of a substring in a string
# author: @0xCrimsonSky
# example: count_occurrences "banana" "a" -> "3"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected text and substring arguments"

    text, sub = args
    if not isinstance(text, str) or not isinstance(sub, str):
        return "Error: expected string arguments"

    return str(text.count(sub))
