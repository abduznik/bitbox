# tool: is_lowercase
# description: Checks if a string is all lowercase
# author: @insisong
# example: is_lowercase "hello" → "True"


def run(*args) -> str:
    text = args[0]
    return str(text.islower())
