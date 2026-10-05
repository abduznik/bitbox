# tool: pig_latin
# description: Convert words in a string to Pig Latin
# author: @ShauryaPrakashVerma
# example: pig_latin "hello world" -> "ellohay orldway"


def run(*args) -> str:

    if len(args) < 1:
        return "Error: requires a string argument"
    text = args[0]
    if not isinstance(text, str):
        return "Error: argument must be a string"
    words = text.split()


    return " ".join(word[1:] + word[0] + "ay" for word in words)