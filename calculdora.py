class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        suma = self.num1 + self.num2
        return f"{self.num1} + {self.num2} = {suma}"

    def restar(self):
        resta = self.num1 + self.num2
        return f"{self.num1} - {self.num2} = {resta}"

    def multiplicar(self):
        multi = self.num1 * self.num2
        return f"{self.num1} x {self.num2} = {multi}"

    def dividir(self):
        div = self.num1 / self.num2
        return f"{self.num1} / {self.num2} = {div}"

    def div_enteros(self):
        div_ent = self.num1 // self.num2
        return f"{self.num1} // {self.num2} = {div_ent}"

    def potenciar(self):
        poten = self.num1 ** self.num2
        return f"{self.num1} ** {self.num2} = {poten}"

    def verificar(self):
        if self.num1 != int:
            raise Exception("El número debe ser entero")
        elif self.num2 != int:
            raise Exception("El número debe ser entero")

    def menu(self):
        opcion = "0"
        while not (opcion == "7"):
            print("----------------------")
            print("1: SUMA")
            print("2: RESTA")
            print("3: MULTIPLICACIÓN")
            print("4: DIVISIÓN")
            print("5: DIVISIÓN ENTEROS")
            print("6: POTENCIA")
            print("7: Salir")
            print("---------------------")

            opcion = input("Elije una opción: ")
            if opcion == "1":
                print(self.sumar())
                print()
            elif opcion == "2":
                print(self.restar())
                print()
            elif opcion == "3":
                print(self.multiplicar())
                print()
            elif opcion == "4":
                print(self.dividir())
                print()
            elif opcion == "5":
                print(self.div_enteros())
                print()
            elif opcion == "6":
                print(self.potenciar())
                print()
            elif opcion == "7":
                print("Ha terminado el programa")
                print()
            else:
                print("No existe, elija otra opcion")
                print()


fnum1 = int(input("Dame un número: "))
fnum2 = int(input("Dame otro número: "))
calc = Calculadora(fnum1, fnum2)
calc.menu()
24,375