# tool: count_negative
# description: Count negative numbers in a comma-separated list
# author: @pardhusriparupudi
# example: count_negative "-1,2,-3" -> "2"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one comma-separated list."

    try:
        nums = [float(num.strip()) for num in str(args[0]).split(",")]
    except ValueError:
        return "Error: Please provide a list of valid numbers."

    return str(sum(num < 0 for num in nums))
