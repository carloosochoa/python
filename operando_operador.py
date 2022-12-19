def burbuja(operacion):
    resultado = 0
    simbolo = operacion.split(" ")
    if simbolo[1] in ["+", "*", "**", "-", "/"]:
        if simbolo[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            if simbolo[2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                num1 = int(simbolo[0])
                num2 = int(simbolo[2])
                valor = simbolo[1]
                if valor == "+":
                    resultado = num1 + num2

                elif valor == "-":
                    resultado = num1 - num2

                elif valor == "*":
                    resultado = num1 * num2

                elif valor == "/":
                    resultado = num1 / num2
                elif valor == "**":
                    resultado = num1 ** num2
                return f"{simbolo[0]} {simbolo[1]} {simbolo[2]} = {resultado}"
            else:
                print("El operando2 debe ser un número")
        else:
            print("El operando1 debe ser un número")
    else:
        print("El operador es incorrecto")


operacion = input("Introduce la operacion: ")
while operacion != "salir":
    print(burbuja(operacion))
    operacion = input("Introduce la operacion: ")