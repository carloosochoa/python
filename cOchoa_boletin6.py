def cadena_alaquasera(cadena):
    pos_vocal = 1
    pos_cons = 2
    pos_num = 3
    pos_guion = 4
    pos = 0

    for i in cadena:
        pos += 1
        if pos == pos_vocal:
            pos_vocal += 4
            if i not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
                return False
        elif pos == pos_cons:
            pos_cons += 4

            if i not in ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b",
                         "n", "m"]:
                return False
        elif pos == pos_num:
            pos_num += 4

            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False
        elif pos == pos_guion:
            pos_guion += 4
            if i not in ["-"]:
                return False

    return True


fcadena = input("Cadena: ")
print(f"cadena_alaquasera({fcadena}) --> {cadena_alaquasera(fcadena)}")
