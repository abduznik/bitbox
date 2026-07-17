# tool: factorial
# description: Find factorial of number
# author: @persianflower
# example: factorial "5" -> "120"

import math 

def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])
   number = int(args[0])
   fact = math.factorial(number)
   return str(fact)
    