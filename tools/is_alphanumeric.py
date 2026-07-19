# tool: is_alphanumeric
# description: Checks whether a string contains only letters and digits
# author: @persianflower
# example: is_alphanumeric "hello123" -> "True"


def run(*args) -> str:
    text = args[0]
    return text.isalnum()