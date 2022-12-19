
def menu():
    tamany = 3
    caracter = "O"

    op = 0
    while op != 6:
        print()
        print("1) Canvi de tamany: ")
        print("2) Canvi de caràcter: ")
        print("3) Mostrar ona de tipus 1")
        print("4) Mostrar ona de tipus 2")
        print("5) Mostrar ona de tipus 3")
        print("6) Salir")
        op = int(input("Elije una opcion: "))
        if op == 1:
            print()
            tamany = int(input("Canvi de tamany: "))
        elif op == 2:
            caracter = input("Canvi de caracter: ")
        elif op == 3:
            print()
            print(f"L'ona de tipus 1 serà(tamany {tamany} i caràcter {caracter})")
            print(f" {caracter}"*tamany)
            print(f"{caracter} "*tamany)
        elif op == 4:
            print()
            print(f"L'ona de tipus 2 serà(tamany {tamany} i caràcter {caracter})")
            print(f"  {caracter}     " * tamany)
            print(f" {caracter}{caracter}{caracter}    " * tamany)
            print(f"{caracter}{caracter}{caracter}{caracter}{caracter}   " * tamany)
        elif op == 5:
            print()
            print(f"L'ona de tipus 2 serà(tamany {tamany} i caràcter {caracter})")
        elif op == 6:
            break
        else:
            print("Opcion equivocada")

menu()