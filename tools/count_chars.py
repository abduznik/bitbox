# tool: count_chars
# description: Counts the number of characters in a string (excluding spaces)
# author: @prakhargaba007
# example: count_chars "hello world" → "10"


def run(*args) -> str:
    text = args[0]
    count = sum(1 for char in text if char != ' ')
    return str(count)
