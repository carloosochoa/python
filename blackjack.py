import random
import time


def limpiar_pantalla():
    print("\n" * 50)


def carta():
    carta1 = random.randint(1, 13)
    return carta1


def juego():
    c_puntos = 0
    j1_puntos = 0
    j1_historial = []
    c_historial = []
    palos = ["Tréboles", "Rombos", "Corazones", "picas"]
    parar = ""
    print("BLACKJACK 2023")
    j1 = input("Dame tu nombre: ")
    limpiar_pantalla()
    print(f"Hola {j1} soy el Crupier, vamos a jugar. Suerte!")
    print()
    i = 0
    while j1_puntos < 21 or parar == "n":
        time.sleep(3)
        limpiar_pantalla()
        if i == 0:
            if c_puntos > 21:
                print("Has ganado!")
                break
            else:
                print("Turno del Crupier")
                tirada_c = carta()
                palo = random.choice(palos)
                if tirada_c == 11:
                    c_puntos += 10
                    c_historial.append(f"J de {palo}")
                elif tirada_c == 12:
                    c_puntos += 10
                    c_historial.append(f"Q de {palo}")
                elif tirada_c == 13:
                    c_historial.append(f"K de {palo}")
                elif tirada_c == 1:
                    c_puntos += 11
                    c_historial.append(f"As de {palo}")
                else:
                    c_puntos += tirada_c
                    c_historial.append(f"{tirada_c} de {palo}")
                print(f"Crupier: {c_historial} : {c_puntos} puntos")
                print()
            i = 1
        elif i == 1 and not parar == "n":
            if j1_puntos > 21:
                print("Has perdido, te has pasado de 21")
                break
            else:
                print(f"Turno de {j1}")
                tirada_c = carta()
                palo = random.choice(palos)
                if tirada_c == 11:
                    j1_puntos += 10
                    j1_historial.append(f"J de {palo}")
                elif tirada_c == 12:
                    j1_puntos += 10
                    j1_historial.append(f"Q de {palo}")
                elif tirada_c == 13:
                    j1_puntos += 10
                    j1_historial.append(f"K de {palo}")
                elif tirada_c == 1:
                    j1_puntos += 11
                    c_historial.append(f"As de {palo}")
                else:
                    j1_puntos += tirada_c
                    j1_historial.append(f"{tirada_c} de {palo}")
                print(f"{j1}: {j1_historial}: {j1_puntos} puntos")
                parar = input("quieres otra carta? (s/n)")
            i = 0
    if c_puntos > 21 or (j1_puntos == 21 and c_puntos != 21):
        print("Has ganado!")
    elif j1_puntos > 21:
        print("Te has pasado de 21, has perdido")
    if j1_puntos < 21 and c_puntos < 21:
        if (21 - j1_puntos) < (21 - c_puntos):
            print("Has ganado!")
        elif (21 - j1_puntos) > (21 - c_puntos):
            print("El crupier ha estado mas cerca de 21")
            print(f"Crupier: {c_puntos}")
            print(f"{j1}: {j1_puntos}")
        elif j1_puntos == c_puntos:
            print("Empate!")


juego()
