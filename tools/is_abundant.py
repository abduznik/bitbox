# tool: is_abundant
# description: Check if a number is abundant (sum of divisors > n)
# author: @rmanojgowda
# example: is_abundant "12" -> True


def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])
    text = args[0]
    try:
        n = int(text)

        if n <= 0:
            return "False"
        sum_of_divisors = 0

        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i

        if sum_of_divisors > n:
            return "True"
    except ValueError:
        return "Error : input must be number"
    return "False"
