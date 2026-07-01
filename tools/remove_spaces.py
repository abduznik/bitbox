# tool: remove_spaces
# description: Removes all spaces from a string
# author: @insisong
# example: remove_spaces "hello world" → "helloworld"


def run(*args) -> str:
    text = args[0]
    return text.replace(" ", "")
