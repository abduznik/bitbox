# tool: starts_with
# description: checks if a string starts with a given prefix
# author: @navaneethsankar07
# example: starts_with("hello world", "hello") returns True


def run(*args) -> str:
    string = args[0]
    prefix = args[1]
    return str(string.startswith(prefix))
