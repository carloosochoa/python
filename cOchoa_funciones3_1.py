def media(flista):
    median = sum(flista) / len(flista)
    return median


lista1 = [2, 4, 8]
lista2 = [9, 10, 2, 6, 8, 8]
lista3 = [100, 102, 200, 500, 600, 700, 900, 1000]

print(media(lista1))
print(media(lista2))
print(media(lista3))
