# tool: sentence_count
# description: Counts the number of sentences in a given text(by ., !, or ?)
# author: @navaneethsankar07
# example: sentence_count("Hello! How are you? I am fine.") returns "3"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = args[0]
    count = 0

    for char in text:
        if char in '.!?':
            count += 1
            
    return str(count)
