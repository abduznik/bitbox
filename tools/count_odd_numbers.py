# tool: count_odd_numbers
# description: Count odd numbers in a list
# author: @jaideepkrishna2008-ui
# example: count_odd_numbers "1,2,3,4,5" -> "3"


def run(*args) -> str:
    if not args or not args[0].strip():
        return "0"
    numbers = [int(x.strip()) for x in args[0].split(",") if x.strip()]
    count = sum(1 for n in numbers if n % 2 != 0)
    return str(count)
