def es_palindrom(fcadena):
    if fcadena == fcadena[::-1]:
        return True
    else:
        return False


cadena = input("Cadena: ")
print(f"es_palindrom({cadena}) --> {es_palindrom(cadena)}")
