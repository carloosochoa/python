import random


def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def jugar():
    j1 = input("Jugador 1: ")
    j2 = input("Jugador 2: ")
    rondas_para_ganar = int(input("Puntuación para ganar: "))
    rondas_j1 = 0
    rondas_j2 = 0
    while rondas_j1 < rondas_para_ganar and rondas_j2 < rondas_para_ganar:
        dado1_j1, dado2_j1 = lanzar_dados()
        dado1_j2, dado2_j2 = lanzar_dados()
        print("---------")
        print(f"Resultado de los dados de {j1}: [{dado1_j1}, {dado2_j1}]")
        print(f"Resultado de los dados de {j2}: [{dado1_j2}, {dado2_j2}]")

        if dado1_j1 > dado1_j2 and dado2_j1 > dado2_j2:
            rondas_j1 += 1
            print(f"{j1} gana la ronda")
            print("-------")
            print(f"Puntuación {j1}: {rondas_j1}")
            print(f"Puntuación {j2}: {rondas_j2}")
            print("--------")
        elif dado1_j1 > dado1_j2 and dado2_j1 < dado2_j2:
            print("Empate")
            print(f"Puntuación {j1}: {rondas_j1}")
            print(f"Puntuación {j2}: {rondas_j2}")
        elif dado1_j1 < dado1_j2 and dado2_j1 > dado2_j2:
            print("Empate")
            print(f"Puntuación {j1}: {rondas_j1}")
            print(f"Puntuación {j2}: {rondas_j2}")
        elif dado1_j1 == dado1_j2 and dado2_j1 == dado2_j2:
            print("Empate")
        else:
            rondas_j2 += 1
            print(f"{j2} gana la ronda")
            print("--------")
            print(f"Puntuación {j1}: {rondas_j1}")
            print(f"Puntuación {j2}: {rondas_j2}")
    if rondas_j1 > rondas_j2:
        print(f"{j1} gana la partida")
    else:
        print(f"{j2} gana la partida")
    print("............")
    print(f"Puntuación final: ")
    print(f"{j1}: {rondas_j1}")
    print(f"{j2}: {rondas_j2}")


jugar()
