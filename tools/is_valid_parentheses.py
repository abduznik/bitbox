# tool: is_valid_parentheses
# description: Check whether parentheses, square brackets and braces are balanced
# author: @Wkhanex
# example: is_valid_parentheses "([])" -> "True"


def run(*args) -> str:
    """Check bracket nesting while ignoring characters that are not brackets."""
    if len(args) != 1:
        raise ValueError("expected one string")
    expected = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in args[0]:
        if character in expected:
            stack.append(expected[character])
        elif character in ")]}":
            if not stack or stack.pop() != character:
                return "False"
    return str(not stack)
