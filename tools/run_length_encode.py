# tool: run_length_encode
# description: Encodes a string using run-length encoding. Use -s to avoid encoding single characters.
# author: @marcosistoocommon
# example: run_length_encode "aaaabbc" -> "4a2b1c"; run_length_encode "aaaabbc" -s -> "4a2bc"

def run(*args) -> str:
    if not args:
        return "Error: Please introduce a String"
    if len(args) >2:
        return "Error: Too many arguments. Only valid tag after a String is '-s' for shortened version"
    input_string = args[0]
    short_flag = args[1] if len(args) == 2 else None
    encoded_string = []
    count = 1
    prev_char = input_string[0]

    for char in input_string[1:]:
        if char == prev_char:
            count += 1
        else:
            if short_flag == "-s" and count == 1:
                encoded_string.append(prev_char)
            else:
                encoded_string.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    if short_flag == "-s" and count == 1:
        encoded_string.append(prev_char)
    else:
        encoded_string.append(f"{count}{prev_char}")

    return ''.join(encoded_string)