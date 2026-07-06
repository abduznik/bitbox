# tool: seconds_to_hms
# description: Converts a number of seconds to h:mm:ss format
# author: @George4177
# example: seconds_to_hms "3661" -> "1:01:01"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: expected exactly one argument: seconds"

    raw_seconds = str(args[0]).strip()
    try:
        total_seconds = int(raw_seconds)
    except ValueError:
        return "Error: seconds must be an integer"

    if total_seconds < 0:
        return "Error: seconds must be non-negative"

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"
