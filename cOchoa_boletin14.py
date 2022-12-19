def vocales(fcadena):
    a, e, letra_i, o, u = 0, 0, 0, 0, 0
    for i in fcadena:
        if i == "a":
            a += 1
        elif i == "e":
            e += 1
        elif i == "i":
            letra_i += 1
        elif i == "o":
            o += 1
        elif i == "u":
            u += 1
    print(f"a : {a}")
    print(f"e : {e}")
    print(f"i : {letra_i}")
    print(f"o : {o}")
    print(f"u : {u}")


cadena = input("Cadena: ")
while True:
    if cadena == "end":
        break
    vocales(cadena)
    cadena = input("Cadena: ")
