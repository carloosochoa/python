def vocales(cadena):
    a, e, i, o, u = 0,0,0,0,0
    for i in cadena:
        if cadena[i] == "a":
            a += 1
