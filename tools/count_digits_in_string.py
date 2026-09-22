# tool: count_digits_in_string
# description: Count digit characters in a string
# author: @jaideepkrishna2008-ui
# example: count_digits_in_string "abc123" -> "3"


def run(*args) -> str:
    if not args:
        return "0"
    text = args[0]
    count = sum(1 for c in text if c.isdigit())
    return str(count)
