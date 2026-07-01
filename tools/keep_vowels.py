# tool: keep_vowels
# description: Keeps only the vowels from a string
# author: @insisong
# example: keep_vowels "hello world" → "eoo"


def run(*args) -> str:
    text = args[0]
    return "".join(ch for ch in text if ch.lower() in "aeiou")
