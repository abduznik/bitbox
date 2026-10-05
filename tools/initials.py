# tool: initials
# description: First letter of each word in a string
# author: @ShauryaPrakashVerma
# example: initials "John Ronald Tolkien" -> "JRT"


def run(*args) -> str:

    if len(args) < 1:
        return "Error: requires a string argument"

    text = args[0]

    if not isinstance(text, str):
        return "Error: argument must be a string"

    words = text.split()

    return "".join(word[0] for word in words)