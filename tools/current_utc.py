# tool: current_utc
# description: Returns the current UTC date and time as an ISO 8601 string
# author: @PriyadharshiniRVP
# example: current_utc -> "2024-06-30T12:00:00+00:00"

from datetime import datetime, timezone


def run(*args) -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()