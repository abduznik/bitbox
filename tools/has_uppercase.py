# tool: has_uppercase
# description: Check if a string contains at least one uppercase letter
# author: @ncmoore55
# example: has_uppercase "Hello" -> "True"


def run(*args) -> str:
    text = args[0]

    for letter in text:
        if letter.isupper():
            return "True"
    return "False"


