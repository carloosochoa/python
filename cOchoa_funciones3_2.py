def media(flista):
    median = sum(flista) / len(flista)
    return median


lista = []
num = 1
while num != 0:
    num = int(input("Número: "))
    if num == 0:
        break
    lista.append(num)

print(f"La media de {lista} es: ")
print(media(lista))
