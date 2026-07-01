# tool: swap_case
# description: Swaps the case of each character in a string
# author: @insisong
# example: swap_case "Hello World" → "hELLO wORLD"


def run(*args) -> str:
    text = args[0]
    return text.swapcase()
