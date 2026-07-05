# tool: seconds_to_hms
# description: Converts a number of seconds to h:mm:ss format
# author: @its-Sohan
# example: seconds_to_hms "3661" -> "1:01:01"


def run(*args) -> str:
    total = int(args[0])
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h}:{m:02d}:{s:02d}"
