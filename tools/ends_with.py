# tool: ends_with
# description: Checks if a string ends with a given suffix
# author: @m-kras
# example: ends_with "hello" "lo" -> "True"


def run(*args) -> str:
    text = args[0].strip()
    suffix = args[1].strip()
    if text.endswith(suffix):
        return "True"
    else:
        return "False"
