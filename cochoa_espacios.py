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


def consonante(fcadena) -> bool:
    if fcadena not in ["a", "e", "i", "o", "u"]:
        return True
    return False


def consonantes(fcadena) -> int:
    contador = 0
    for i in range(len(fcadena)):
        if fcadena[i] not in ["a", "e", "i", "o", "u"] and fcadena[i] not in [" "]:
            contador += 1
    return contador


def espacio(fcadena) -> bool:
    if fcadena in [" "]:
        return True
    else:
        return False


def espacios(fcadena) -> int:
    contador = 0
    for i in range(len(fcadena)):
        if fcadena[i] in [" "]:
            contador += 1
    return contador


cadena = input("Cadena: ")

print("El texto tiene: ")
print(f"{vocales(cadena)} vocales")
print(f"{consonantes(cadena)} consonantes")
print(f"{espacios(cadena)} espacios en blanco")
