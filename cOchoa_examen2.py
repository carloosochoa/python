


def buscar(palabra, fbuscar):
    pos = 0
    for i in palabra:
        pos += 1
        if fbuscar == palabra:
            print("Has ganado")
            break
        elif fbuscar[pos] in palabra:
            print(f"Alguna de las letras de la palabra {fbuscar} están en la palabra a buscar")
            break
        else:
            print(f"La palabra {fbuscar} no contiene  ninguna letra de la palabra")
            break


def jugar(fpalabra):

    asteriscos = "*"
    mult = asteriscos * len(palabra)
    while True:
        print(f"La palabra a buscar es: {mult}")
        i = 1
        intento1 = 1
        intento2 = 1
        if i == 1:
            print(f"JUGADOR 1: Es tu intento {intento1}")
            busca = input("Indica tu palabra: ")
            i = 2
            intento1 += 1
            buscar(fpalabra, busca)

            if fpalabra == busca:
                break

        if i == 2:
            print(f"JUGADOR 2: Es tu intento {intento2}")
            busca = input("Indica tu palabra: ")
            i = 1
            intento2 += 1
            buscar(fpalabra, busca)

            if fpalabra == busca:
                break


print("JUEZ (Los jugadores no deben ver la palabra)")
palabra = input("Introduce la palabra a buscar: ")
jugar(palabra)
