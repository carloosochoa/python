def cuadrado(fnum):
    for i in range(fnum):
        for j in range(fnum):
            print(f"{fnum} ", end="")
        print()


num = int(input("Num: "))
cuadrado(num)
