tamanyo = 5


def menu() -> None:
    print("1) Cambiar tamaño  (5)")
    print("2) Imprimir triangulo")
    print("3) Imprimir quadrado")
    print("4) Salir del programa")


def cambio() -> int:
    tamano = int(input("Dime un tamanyo: "))
    return tamano


def triangulo(ftamanyo) -> None:
    for i in range(0, ftamanyo + 1):
        print("*" * i)


def cuadrado(ftamanyo) -> None:
    for i in range(0, ftamanyo):
        for j in range(0, ftamanyo):
            print("*", end=" ")
        print()


op = 0

while op != 4:
    menu()
    op = int(input("Opcion: "))
    if op == 1:
        tamanyo = cambio()
    elif op == 2:
        triangulo(tamanyo)
    elif op == 3:
        cuadrado(tamanyo)
    elif op == 4:
        break
