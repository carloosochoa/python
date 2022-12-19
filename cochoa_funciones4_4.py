def final_igual(fcadena1, fcadena2):
    reves1 = fcadena1[::-1]
    reves2 = fcadena2[::-1]
    pos = 0
    igual = ""
    for i in range(len(fcadena1)):
        if reves1[pos] == reves2[pos]:
            igual = igual + reves1[i]
        else:
            break
        pos += 1

    igual1 = igual[::-1]
    return igual1


cadena1 = input("Cadena 1: ")
cadena2 = input("Cadens 2: ")

print(f"final_igual({cadena1},{cadena2}) -> {final_igual(cadena1,cadena2)}")
