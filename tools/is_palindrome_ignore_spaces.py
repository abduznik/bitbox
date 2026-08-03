# tool: is_palindrome_ignore_spaces
# description: Checks if a string is a palindrome ignoring spaces
# author: @Jesulac
# example: is_palindrome_ignore_spaces "nurses run" -> "True"


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    # Only whitespace is ignored (punctuation is kept, unlike is_palindrome).
    # Comparison is case-insensitive, matching the existing is_palindrome tool.
    cleaned = "".join(args[0].split()).lower()
    return str(cleaned == cleaned[::-1])
