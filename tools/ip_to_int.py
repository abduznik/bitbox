# tool: ip_to_int
# description: Convert an IPv4 address to an integer.
# author: @masyarakatai
# example: ip_to_int "192.168.0.1" -> "3232235521"

import ipaddress


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        return str(int(ipaddress.IPv4Address(args[0].strip())))
    except (AttributeError, ValueError):
        return "Error: Invalid IPv4 address."
