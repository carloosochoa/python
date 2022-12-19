def media(flista):
    median = sum(flista) / len(flista)

    return median


def mayor(flista):
    mayor_n = flista[0]
    for i in flista:
        if i > mayor_n:
            mayor_n = i
    return mayor_n


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
