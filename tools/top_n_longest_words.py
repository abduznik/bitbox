# tool: top_n_longest_words
# description: Returns the N longest words from a text.
# author: @1998LJ
# example: top_n_longest_words "the quick brown fox jumps" "2" -> "quick,jumps"

import re


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide text and a non-negative integer."

    text = str(args[0])
    try:
        n = int(str(args[1]).strip())
    except ValueError:
        return "Error: Second argument must be a non-negative integer."

    if n < 0:
        return "Error: Second argument must be a non-negative integer."
    if n == 0:
        return ""

    words = re.findall(r"\b\w+(?:[-']\w+)*\b", text, flags=re.UNICODE)
    longest = sorted(
        words,
        key=lambda word: (len(word), word.casefold()),
        reverse=True,
    )[:n]
    return ",".join(longest)
