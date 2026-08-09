# tool: Collatz steps
# description: A tool which counts the steps to reach the next number in the Collatz sequence
# author: @LinuxLarper
# example: example_tool "input" -> "output"


def run(*args) -> str:
    # args[0] is the first argument, args[1] is the second, etc.
    # Example with two args: text = args[0], length = int(args[1])

    if len(args) != 1 or str.isdigit(args[0]) == False or int(args[0]) < 1:
        return("This Tool Requires one positive interger")
    
    n = int(args[0])
    steps = 0

    while n != 1:
        steps+=1
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3+1

    return steps
