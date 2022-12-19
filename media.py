def media(fnum1, fnum2, fnum3, fnum4):
    mediarit = (fnum1 + fnum2 + fnum3 + fnum4) / 4
    return mediarit


num1 = int(input("Dame un número: "))
num2 = int(input("Dame un número: "))
num3 = int(input("Dame un número: "))
num4 = int(input("Dame un número: "))
print(media(num1, num2, num3, num4))
