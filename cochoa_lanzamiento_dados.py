import random


def lanzamiento():
    return random.randint(1, 6)


def juego(ftiradas):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    for i in range(ftiradas):
        dado = lanzamiento()
        if dado == 1:
            cont1 += 1
        elif dado == 2:
            cont2 += 1
        elif dado == 3:
            cont3 += 1
        elif dado == 4:
            cont4 += 1
        elif dado == 5:
            cont5 += 1
        else:
            cont6 += 1

    porcen1 = (cont1 / ftiradas) * 100
    porcen2 = (cont2 / ftiradas) * 100
    porcen3 = (cont3 / ftiradas) * 100
    porcen4 = (cont4 / ftiradas) * 100
    porcen5 = (cont5 / ftiradas) * 100
    porcen6 = (cont6 / ftiradas) * 100

    print(f"1 -> {cont1} ({porcen1:.2f}%)")
    print(f"2 -> {cont2} ({porcen2:.2f}%)")
    print(f"3 -> {cont3} ({porcen3:.2f}%)")
    print(f"4 -> {cont4} ({porcen4:.2f}%)")
    print(f"5 -> {cont5} ({porcen5:.2f}%)")
    print(f"6 -> {cont6} ({porcen6:.2f}%)")


tiradas = int(input("Indica el numero de lanzamientos del dado: "))
juego(tiradas)
