# tool: ngrams
# description: Generates character n-grams from a string.
# author: @1998LJ
# example: ngrams "hello" "2" -> "he,el,ll,lo"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide text and a positive integer."

    text = str(args[0])
    try:
        n = int(str(args[1]).strip())
    except ValueError:
        return "Error: Second argument must be a positive integer."

    if n <= 0:
        return "Error: Second argument must be a positive integer."
    if n > len(text):
        return ""

    return ",".join(
        text[index:index + n]
        for index in range(len(text) - n + 1)
    )
