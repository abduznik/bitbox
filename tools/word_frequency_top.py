# tool: word_frequency_top
# description: Most frequent whitespace-separated word (case-sensitive; first occurrence breaks ties)
# author: @00200200
# example: word_frequency_top "the cat the dog the" -> "the:3"

from collections import Counter


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    counts = Counter(args[0].split())
    if not counts:
        return ""
    word, count = counts.most_common(1)[0]
    return f"{word}:{count}"
