from ipaddress import ip_address


class Ip:
    def __init__(self, ip):
        self.ip = ip

        lista = self.ip.split(".")
        if len(lista) != 4:
            raise Exception("La IP tiene que contener 4 octetos")

        self.__primero = int(lista[0])
        if self.__primero < 0 or self.__primero > 255:
            raise Exception("El primero octeto debe estar entre 0 y 255")

        self.__segundo = int(lista[1])
        if self.__segundo < 0 or self.__segundo > 255:
            raise Exception("El segundo octeto debe estar entre 0 y 255")

        self.__tercero = int(lista[2])
        if self.__tercero < 0 or self.__tercero > 255:
            raise Exception("El tercer octeto debe estar entre 0 y 255")

        self.__cuarto = int(lista[3])
        if self.__cuarto < 0 or self.__cuarto > 255:
            raise Exception("El cuarto octeto debe estar entre 0 y 255")


    def priv_publi(self):
        if ip_address(self.ip).is_private:
            return f"La Ip: {self.ip} es privada"
        else:
            return f"La IP {self.ip} es pública"

    def mostrar(self):
        opcion = "0"
        while not (opcion == "7"):
            print("----------------------")
            print("1: primer octeto")
            print("2: segundo octeto")
            print("3: tercer octeto")
            print("4: cuarto octeto")
            print("5:  ip entera")
            print("6:Privada o pública")
            print("7: Salir")
            print("---------------------")

            opcion = input("Elije una opción: ")
            if opcion == "1":
                print(self.__primero)
                print()
            elif opcion == "2":
                print(self.__segundo)
                print()
            elif opcion == "3":
                print(self.__tercero)
                print()
            elif opcion == "4":
                print(self.__cuarto)
                print()
            elif opcion == "5":
                print(self.ip)
                print()
            elif opcion == "6":
                print(self.priv_publi())
                print()
            elif opcion == "7":
                print("Salir")
                print()


ip = input("dame una dirección IP: ")
ip1 = Ip(ip)
ip1.mostrar()
