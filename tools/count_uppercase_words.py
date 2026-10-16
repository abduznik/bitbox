# tool: count_uppercase_words
# description: Count whitespace-separated words starting with an uppercase letter
# author: @Wkhanex
# example: count_uppercase_words "Hello world" -> "1"


def run(*args) -> str:
    """Count words whose first character is an uppercase Unicode letter."""
    if len(args) != 1:
        raise ValueError("expected one string")
    return str(sum(word[0].isupper() for word in args[0].split()))
