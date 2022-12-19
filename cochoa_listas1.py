def iguales(flista1, flista2) -> list:
    igual = []
    if len(flista1) < len(flista2):
        menor = flista1
        mayor = flista2
    else:
        menor = flista2
        mayor = flista1
    pos = 0
    for i in range(len(menor)):
        if mayor[pos] in menor:
            igual.append(mayor[i])
        pos += 1
    return igual


lista1 = input("Lista 1:")
lista2 = input("Lista 2: ")
print(f"iguales({lista1},{lista2}) -> {iguales(lista1,lista2)}")
