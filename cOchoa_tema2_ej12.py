def dni_correcto(fdni):
    if len(fdni) == 9:
        num_dni = fdni[:8]
        letra = fdni[8]
        if letra.isalpha() and letra.isupper() and num_dni.isdecimal() and validar_letra(fdni) == letra:
            # isalpha() = si es una letra del abecedario
            # isupper() = si es mayúscula
            # isdecimal() = si es número
            return True
        else:
            return False
    else:
        return False


def validar_letra(fdni):
    num_dni = int(fdni[:8])
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    valor = num_dni % 23
    letra_correcta = letras[valor]
    return letra_correcta


dni = ""

while dni != "0":
    dni = input("Dame tu DNI: ")
    if dni == "0":
        break
    if dni_correcto(dni):
        print(f"El DNI [{dni}] es correcto")
    else:
        print(f"El DNI [{dni}] es incorrecto")
        print(F"La letra correcta es {validar_letra(dni)}")
