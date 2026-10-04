# tool: word_frequency_top
# description: Find the most frequent word in a text
# author: @abduznik
# example: word_frequency_top "the cat the dog the" -> "the:3"


import re
from collections import Counter


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    words = re.findall(r"\w+", str(args[0]).lower())
    if not words:
        return ""
    word, count = Counter(words).most_common(1)[0]
    return f"{word}:{count}"
