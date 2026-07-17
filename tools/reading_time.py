# tool: reading_time
# description: Estimates reading time in minutes (assuming 200 wpm)
# author: @PurpleSwtr
# example: reading_time "400 words of text here" -> "2"


def run(*args) -> str:
    text = args[0]
    word_count = len(text.strip().split())
    if word_count == 0:
        return "0"
    minutes = (word_count + 100) // 200
    return str(minutes)
