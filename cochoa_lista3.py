def no_aparecen(flista1, flista2) -> list:
    desig = []
    for num_list in flista1:
        if num_list not in flista2:
            desig.append(num_list)
    return desig


lista1 = []
lista2 = []
while True:
    num = int(input("Lista 1:Inserta un número: "))
    if num == 0:
        break
    lista1.append(num)

while True:
    num = int(input("Lista2:Inserta un número: "))
    if num == 0:
        break
    lista2.append(num)

print(f"lista 1: {lista1}")
print(f"Lista2: {lista2}")
print(no_aparecen(lista1, lista2))
