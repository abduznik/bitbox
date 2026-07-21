# tool: md5_hash
# description: Computes the MD5 hex digest of a string
# author: @Solaris-star
# example: md5_hash "hello" -> "5d41402abc4b2a76b9719d911017c592"

import hashlib


def run(*args) -> str:
    text = " ".join(args)
    return hashlib.md5(text.encode("utf-8")).hexdigest()

