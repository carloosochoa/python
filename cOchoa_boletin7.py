def cadena_alaquasera(cadena):
    pos = 0

    for i in cadena:
        pos += 1
        if pos % 4 == 0:
            if i not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
                return False
        elif pos % 4 == 1:
            if i not in ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b",
                         "n", "m"]:
                return False
        elif pos % 4 == 2:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False
        elif pos % 4 == 3:
            if i not in ["-"]:
                return False
    return True


fcadena = input("Cadena: ")
while True:
    if fcadena == "castell":
        break
    print(f"cadena_alaquasera({fcadena}) --> {cadena_alaquasera(fcadena)}")
    fcadena = input("Cadena: ")
