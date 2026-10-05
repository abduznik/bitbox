# tool: is_isogram
# description: Checks if a word is an isogram (no repeating letters).
# author: @navaneethsankar07
# example: is_isogram("isogram") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = args[0]
    return str(len(set(text)) == len(text))
