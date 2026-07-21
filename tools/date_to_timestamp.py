# tool: date_to_timestamp
# description: converts a date/time string to a Unix timestamp
# author: @Solaris-star
# example: date_to_timestamp "2020-01-01T00:00:00+00:00" -> "1577836800"

from datetime import datetime, timezone


def run(*args) -> str:
    if not args:
        return "Error: expected a datetime string"
    raw = args[0]
    try:
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        dt = datetime.fromisoformat(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return str(int(dt.timestamp()))
    except ValueError:
        return f"Error: invalid datetime {args[0]}"

