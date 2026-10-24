# tool: cumulative_sum
# description: Calculate the cumulative sum of comma-separated numbers
# author: @shibinshibii
# example: cumulative_sum "1,2,3" -> "1,3,6"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        numbers = args[0].split(",")
        total = 0
        result = []

        for number in numbers:
            total += int(number.strip())
            result.append(str(total))
        return ",".join(result)

    except ValueError:
        return "Error: Expected comma-separated numbers"

