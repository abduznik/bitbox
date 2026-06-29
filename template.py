# tool: example_tool
# description: A short one-line description of what this tool does
# author: @github_username
# example: example_tool "input" -> "output"


def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])
    text = args[0]
    return text
