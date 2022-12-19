fila1 = ["x", "x", "x", "x"]
fila2 = ["x", "x", "x", "x"]
fila3 = ["x", "x", "x", "x"]
fila4 = ["x", "x", "x", "x"]

reserva = ""
print("RESERVA BUTACAS")
print(fila1)
print(fila2)
print(fila3)
print(fila4)
while reserva != "N":

    fila = int(input("Introduce la fila que quieres: "))
    columna = int(input("Introduce la columna: "))

    if 1 < fila > 4:
        print("La fila no es correcta")

    elif 1 < columna > 4:
        print("La fila no es correcta")

    elif fila == 1:
        if fila1[columna] == "O":
            print("La butaca esta ocupada")
        else:
            print("Reserva realizada.")
            reserva = input("Reservar otra? (S/N): ")
            fila1[columna] = "O"

    elif fila == 2:
        if fila2[columna] == "O":
            print("La butaca esta ocupada")
        else:
            fila2[columna] = "O"
            print("Reserva realizada.")
            reserva = input("Reservar otra? (S/N): ")

    elif fila == 3:
        if fila3[columna] == "O":
            print("La butaca esta ocupada")
        else:
            print("Reserva realizada.")
            reserva = input("Reservar otra? (S/N): ")
            fila3[columna] = "O"

    elif fila == 4:
        if fila4[columna] == "O":
            print("La butaca esta ocupada")
        else:
            fila4[columna] = "O"
            print("Reserva realizada.")
            reserva = input("Reservar otra? (S/N): ")

    print()

    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)

print("Gracias!")
