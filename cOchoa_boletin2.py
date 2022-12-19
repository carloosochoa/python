import random


def lanzamiento():
    return random.randint(1, 6)


def juego():
    print("JUEGO DE DADOS")
    j1 = input("Jugador 1: ")
    gana1 = 0
    j2 = input("Jugador 2: ")
    gana2 = 0
    tiradas = int(input("Nº tiradas: "))

    if tiradas < 1:
        print("ERROR: Tienes que tirar al menos 1 vez")
    for i in range(1, tiradas + 1):
        dado = lanzamiento()
        print()
        print(f"Lanzamiento {i}: Ha salido {dado}")
        if dado % 2 == 0:
            gana1 += 1
            print(f"GANA {j1}")
            print(f"MARCADOR: {j1} {gana1} - {j2} {gana2}")
        else:
            gana2 += 1
            print(f"GANA {j2}")
            print(f"MARCADOR: {j1} {gana1} - {j2} {gana2}")
    print()
    print("Se han acabado todas las tiradas.")
    if gana1 > gana2:
        print(f"GANADOR {j1}")
        print(f"MARCADOR: {j1} {gana1} - {j2} {gana2}")
    elif gana2 > gana1:
        print(f"GANADOR {j2}")
        print(f"MARCADOR: {j1} {gana1} - {j2} {gana2}")
    else:
        print("EMPATE")
        print(f"MARCADOR: {j1} {gana1} - {j2} {gana2}")


juego()
