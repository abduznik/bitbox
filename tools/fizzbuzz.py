# tool: fizzbuzz
# description: Returns Fizz, Buzz, FizzBuzz, or the number for an integer.
# author: @1998LJ
# example: fizzbuzz "15" -> "FizzBuzz"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    value = str(args[0]).strip()
    if not value:
        return "Error: Argument cannot be empty."

    try:
        n = int(value)
    except ValueError:
        return "Error: Argument must be an integer."

    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
