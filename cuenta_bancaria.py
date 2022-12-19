ingresos = []
retiradas = []


class CuentaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def ingreso(self):
        fingreso = int(input("Introduce cantidad: "))
        self.saldo = fingreso + self.saldo
        ingresos.append(fingreso)
        print(f"Saldo: {self.saldo}")

    def reintegro(self):
        retirada = int(input("Introduce cantidad: "))
        if retirada > self.saldo:
            print("No hay saldo suficiente")
        else:
            self.saldo = self.saldo - retirada
            retiradas.append(-retirada)
            print(f"Saldo: {self.saldo}")

    def menu(self):
        while True:
            print("1. Ingreso")
            print("2. Retirada")
            print("3. Salir")
            op = int(input("Opcion: "))
            print()
            if op == 1:
                self.ingreso()
            elif op == 2:
                self.reintegro()
            else:
                break
        print(f"Ingresos: {ingresos}")
        print(f"Reintegros: {retiradas}")


cuenta = CuentaBancaria(0)
cuenta.menu()
