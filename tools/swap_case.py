# tool: swap_case
# description: Swaps the case of each character in a string
# author: @Bruce191
# example: example_tool "NeveR_EndinG" -> "nEVEr_eNDINg"


def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])
    text = args[0]

    #loop method if needed
    #result = ""
    # for letter in text:
    #     if letter.isupper():
    #         result += letter.lower()
    #     else:
    #         result += letter.upper()

    #Built in method
    result = text.swapcase()

    return result
