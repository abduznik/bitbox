# tool: remove_vowels
# description: Removes all vowels from a string
# author: @insisong
# example: remove_vowels "hello world" → "hll wrld"


def run(*args) -> str:
    import re

    text = args[0]
    return re.sub(r"[aeiouAEIOU]", "", text)
