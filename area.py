import math


def area_circle(radi):
    area = math.pi * radi ** 2
    return area


radio = 1
while radio != 0:
    radio = int(input("Dame el radio: "))
    print(area_circle(radio))
