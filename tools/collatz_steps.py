# tool:  collatz_steps
# description: Returns the next element of a Collatz sequence for a given number
# author: @MateiB20
# example: collatz_steps "6" -> "3"
def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    num = args[0].lstrip("-")

    if num == "":
        return "Error: Please provide a non-empty input."

    if not num.isdigit():
        return "Error: Please provide a numeric input."

    if int(num)%2==0:
        return str(int(num)//2)
    else:
        return str(int(num)*3+1)
