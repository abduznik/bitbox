# tool: hex_to_decimal
# description: converts hexadecimal to decimal value
# author: @persianflower
# example: hex_to_decimal "ff" -> "255"


def run(*args) -> str:
    text = list(args[0])
    convert=[]
    alpha={"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    j=0
    for i in range(len(text)-1,-1,-1):
        try:
            text[i]=int(text[i])
        except:
            text[i]=alpha.get(text[i])
        finally:
            convert.append(int(text[i])*16**(j))
            j+=1
    return str(sum(convert))
