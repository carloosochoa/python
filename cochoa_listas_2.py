def impares(flista):
    impar = []
    for num_lista in flista:
        if num_lista % 2 != 0:
            impar.append(num_lista)
    return impar


lista = []
while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    lista.append(num)
print(impares(lista))
