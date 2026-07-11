# tool: longest_word
# description: Finds the longest word in a given text
# author: @PurpleSwtr
# example: longest_word "the quick brown fox" -> "quick"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: expected exactly one argument: text"

    text = args[0]
    if not isinstance(text, str):
        return "Error: argument must be a string"

    words = text.split()
    if not words:
        return "Error: text must not be empty"

    return max(words, key=len)
