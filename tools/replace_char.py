# tool: replace_char
# description: Replaces all occurrences of a character in a string
# author: @metric_vac
# example: replace_char "hello" "l" "r" → "herro"


def run(*args) -> str:
    # We expect 3 arguments: the string, the character to replace, and the replacement
    if len(args) < 3:
        return "Error: replace_char requires 3 arguments: text, old_char, new_char"

    text, old, new = args[0], args[1], args[2]
    return text.replace(old, new)
