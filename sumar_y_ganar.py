lista = [50, 4, 28, 33, 12]

print("SUMAR Y GANAR")
print("Vaya sumando todos los numeros: Empezamos por 0.")
resultado = 0
aciertos = 0
suma = 0
for i in range(len(lista)):
    resultado = int(input(f"Más {lista[i]}: "))
    suma += lista[i]
    if resultado == suma:
        aciertos += 1
    else:
        print(f"Te has equivocado pero has acertado {aciertos}")
if suma == sum(lista):
    print("Enhorabuena, has ganado!")
