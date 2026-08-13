# tool: has_lowercase
# description: Check if a string contains at least one lowercase letter
# author: @dreamqwq114-del
# example: has_lowercase "Hello" -> "True"


def run(*args) -> str:
    text = args[0]
    return str(any(c.islower() for c in text))
