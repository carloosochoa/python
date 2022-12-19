tupla = (5, 20, 3, 7, 6, 8)
k = int(input("Cuantos máximos y minimos quieres?: "))

lista = list(tupla)
if len(lista) < 2 * k:
    print(f"No se pueden extraer {k} máximos y mínimos")
else:
    lista.sort()
    tupla2 = tuple(lista[:k] + lista[-k:])
    print(tupla2)
