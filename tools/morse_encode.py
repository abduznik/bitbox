# tool: morse_encode
# description: Encode text into Morse code
# author: @lingeshg18
# example: morse_encode "SOS" -> "... --- ..."



def run(*args) -> str:
    if not args:
        return "Error: please provide text to encode."

    text=args[0].upper()

    MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
    }

    encoded=[]
    for ch in text:
        if ch in MORSE:
            encoded.append(MORSE[ch])
        else:
            return f"Error: unsupported character: {ch}"
    return " ".join(encoded)
