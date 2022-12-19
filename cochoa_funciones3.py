def media(flista):
    median = sum(flista) / len(flista)

    return median


def mayor(flista):
    mayor_n = flista[0]
    for i in flista:
        if i > mayor_n:
            mayor_n = i
    return mayor_n


def menor(flista):
    menor_n = flista[0]
    for i in flista:
        if i < menor_n:
            menor_n = i
    return menor_n


def mediana(flista):
    medio = int(len(flista) / 2)
    if len(flista) % 2 == 0:
        mediana_n = (flista[medio - 1] + flista[medio]) / 2
    else:
        mediana_n = flista[medio]
    return mediana_n


lista = []
num = 1
while num != 0:
    num = int(input("Número: "))
    if num == 0:
        break
    lista.append(num)

print(f"La media de {lista} es: ")
print(media(lista))
print(f"El mayor numero es {mayor(lista)}")
print(f"El menor numero es: {menor(lista)}")
print(f"La mediana es: {mediana(lista)}")
