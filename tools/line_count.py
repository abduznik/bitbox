# tool: line_count
# description: counts the number of lines in a string
# author: @Solaris-star
# example: line_count "a\nb\nc" -> "3"


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    text = args[0]
    if text == "":
        return "0"
    # splitlines() drops a trailing newline, which matches common line-count UX
    return str(len(text.splitlines()))
