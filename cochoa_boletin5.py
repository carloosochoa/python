def ipv6():
    bloque = 1
    print("VERIFICANT IPs v6")
    fip = input("Dame una IPv6: ")
    ip = fip.split(":")
    if len(ip) != 8:
        raise Exception("Menos de 8 bloques")
    validar(ip[0], bloque)
    bloque += 1
    validar(ip[1], bloque)
    bloque += 1
    validar(ip[2], bloque)
    bloque += 1
    validar(ip[3], bloque)
    bloque += 1
    validar(ip[4], bloque)
    bloque += 1
    validar(ip[5], bloque)
    bloque += 1
    validar(ip[6], bloque)
    bloque += 1
    validar(ip[7], bloque)
    print("La IP v6 es correcta")


def validar(ip, bloque):
    num = 0
    letra = 0
    if len(ip) != 4:
        raise Exception(f"Bloque {bloque} no tiene la longitud adecuada")
    for i in ip:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num += 1
        if i in ["A", "B", "C", "D", "E", "F"]:
            letra += 1
    if letra + num != 4:
        raise Exception(f"Bloque {bloque} tiene caracteres incorrectos")


ipv6()
