# tool: digital_root
# description: Compute the digital root of a number
# author: @HarshRajSinghania
# example: digital_root "99" -> "9"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    raw = args[0].strip()
    if raw.startswith("-"):
        raw = raw[1:]

    if raw == "":
        return "Error: Please provide a non-empty input."

    if not raw.isdigit():
        return "Error: Please provide a numeric input."

    n = int(raw)
    if n == 0:
        return "0"
    return str(1 + (n - 1) % 9)
