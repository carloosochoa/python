vocales = ["a", "e", "i", "o", "u"]
vocal = " "

while vocal != "0":
    vocal = input("Dame una vocal: ")
    if vocal in vocales:
        print("Es una vocal")
    else:
        print("No es una vocal")