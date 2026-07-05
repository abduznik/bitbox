# tool: word_frequency
# description: Returns each word and how many times it appears in a string
# author: @its-Sohan
# example: word_frequency "the cat sat on the mat" -> "the: 2, cat: 1, sat: 1, on: 1, mat: 1"


def run(*args) -> str:
    text = args[0]
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return ", ".join(f"{w}: {c}" for w, c in freq.items())
