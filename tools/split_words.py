# tool: split_words
# description: Splits a sentence into words and returns the count.
# author: @1998LJ
# example: split_words("hello world") returns "2"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    val = str(args[0]).strip()
    if not val:
        return "0"

    words = val.split()
    return str(len(words))
