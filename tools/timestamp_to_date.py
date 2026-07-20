# tool: timestamp_to_date
# description: converts a Unix timestamp to an ISO-8601 UTC datetime
# author: @Solaris-star
# example: timestamp_to_date "1577836800" -> "2020-01-01T00:00:00+00:00"

from datetime import datetime, timezone


def run(*args) -> str:
    if not args:
        return "Error: expected a unix timestamp"
    try:
        ts = int(args[0])
    except ValueError:
        return "Error: timestamp must be an integer"
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()

