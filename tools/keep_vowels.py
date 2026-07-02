# tool: keep_vowels
# description: Keeps only the vowels from a string
# author: @openclaw
# example: keep_vowels "hello world" -> "eoo"


def run(*args) -> str:
    text = args[0]
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char in vowels)
