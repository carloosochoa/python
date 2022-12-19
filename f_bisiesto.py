def f_bisiesto(fanyo):
    if fanyo % 4 == 0 and (fanyo % 100 != 0 or fanyo % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


anyo = int(input("Dame un año: "))
print(f_bisiesto(anyo))
