# tool: is_lowercase
# description: Checks if a string is all lowercase
# author: @openclaw
# example: is_lowercase "hello" -> "True"


def run(*args) -> str:
    text = args[0]
    if not text:
        return "False"
    return str(text.islower())
