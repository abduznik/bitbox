# tool: remove_vowels
# description: Removes all vowels from a string
# author: @openclaw
# example: remove_vowels "hello world" -> "hll wrld"


def run(*args) -> str:
    text = args[0]
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)
