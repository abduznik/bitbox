# tool: char_frequency
# description: returns character frequency counts for a string
# author: @Solaris-star
# example: char_frequency "aab" -> "a:2 b:1"

from collections import Counter


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    counts = Counter(args[0])
    # stable order by first appearance then char
    seen = []
    for ch in args[0]:
        if ch not in seen:
            seen.append(ch)
    return " ".join(f"{ch}:{counts[ch]}" for ch in seen)

