# tool: word_char_ratio
# description: Calculates the ratio of letters to total characters
# author: @sajjadlabx
# example: word_char_ratio "hello!" → "0.83"

def run(*args) -> str:
    text = args[0]

    if not text:
        return "0.00"

    ratio = sum(char.isalpha() for char in text) / len(text)
    return f"{ratio:.2f}"
