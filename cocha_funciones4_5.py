def vocal(fcadena) -> bool:
    if fcadena not in ["a", "e", "i", "o", "u"]:
        return False
    return True


def vocales(fcadena) -> int:
    contador = 0
    for i in range(len(fcadena)):
        if fcadena[i] in ["a", "e", "i", "o", "u"]:
            contador += 1
    return contador


cadena_char = input("Dame un carácter: ")
print(f"vocal({cadena_char}) -> {vocal(cadena_char)}")
cadena_string = input("Dame una cadena: ")
print(f"vocales({cadena_string}) -> {vocales(cadena_string)}")
