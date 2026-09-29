# tool: character_appearances
# description: Count occurrences of each character in a string
# author: @DYNOSuprovo
# example: character_appearances "banana" -> "a:3,b:1,n:2"

from collections import Counter


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"

    text = args[0]
    if not isinstance(text, str):
        return "Error: expected a string argument"

    if not text:
        return ""

    counts = Counter(text)
    return ",".join(f"{char}:{count}" for char, count in sorted(counts.items()))
