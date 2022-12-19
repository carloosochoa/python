combi = [7, 13, 21, 37, 46, 49]

fallos = []
for _ in range(6):
    num = int(input("Introduce el numero: "))
    if num != combi:
        fallos.append(num)
if len(fallos) == 0:
    print()
    print("Enhorabuena, ganaste!")
else:
    print()
    print("Lo siento, no has acertado los siguientes números:")
    print(fallos)
