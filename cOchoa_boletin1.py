def validar_ip(fip):
    lista = fip.split(".")
    if len(lista) != 4:
        print(f"La IP: {fip} es incorrecta--> Debe contener 4 bloques")
    primero = int(lista[0])
    segundo = int(lista[1])
    tercero = int(lista[2])
    cuarto = int(lista[3])
    if primero < 0 or primero > 255:
        print(f"La IP: {fip} es incorrecta--> Primer bloque fuera de los limites")
    elif segundo < 0 or segundo > 255:
        print(f"La IP: {fip} es incorrecta--> Segundo bloque fuera de los limites")
    elif tercero < 0 or tercero > 255:
        print(f"La IP: {fip} es incorrecta--> Tercer bloque fuerade los limites")
    elif cuarto < 0 or cuarto > 255:
        print(f"La IP: {fip} es incorrecta--> Cuarto bloque fuera de los limites")
    else:
        print(f"La IP: {fip} es correcta")


ip = input("Dame una IP: ")
validar_ip(ip)
