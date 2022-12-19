def buscar(fcadena, flet1, flet2):
    if flet1 == fcadena[0] and flet2 == fcadena[-1]:
        return True
    else:
        return False


cadena = ""
letra1 = ""
letra2 = ""
while True:
    cadena = input("Cadena: ")

    if cadena == "carlos":
        break
    letra1 = input("Letra1: ")
    letra2 = input("Letra2: ")
    print(buscar(cadena, letra1, letra2))
