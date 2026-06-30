# tool: is_anagram
# description: Checks if two strings are anagrams of each other
# author: @AlexMnrs
# example: is_anagram "listen" "silent" -> "True"


def run(*args) -> str:
    text1 = args[0]
    text2 = args[1]

    normalized1 = "".join(c.casefold() for c in text1 if c.isalnum())
    normalized2 = "".join(c.casefold() for c in text2 if c.isalnum())

    return str(sorted(normalized1) == sorted(normalized2))
