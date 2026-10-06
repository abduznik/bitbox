# tool: truncate_middle
# description: Truncates the given amount of characters from the middle of a string and appends "..."
# author: @marcosistoocommon
# example: truncate "Hello World" "5" → "He...rld"


def run(*args) -> str:
    text = args[0]
    length = int(args[1])
    if len(text) <= length:
        return text
    return text[:length//2] + "..." + text[-length//2:]
