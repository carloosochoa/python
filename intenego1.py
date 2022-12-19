def valor_futuro(fcapital, finteres, fanos):
    for i in range(fanos):
        print("Año ", i, ": ", fcapital * (1 + finteres / 100) ** (i + 1))


def valor_actual(fcapital, finteres, fanos):
    for i in range(fanos):
        print("Año ", -i, ": ", fcapital / (1 + finteres / 100) ** (i + 1))


capital = int(input("Introduce capital: "))
interes = int(input("Introduce un tipo de interés: "))
anyos = int(input("Introduce un número de años: "))
print("VALOR FUTURO")
valor_futuro(capital, interes, anyos)
print("VALOR ACTUAL")
valor_actual(capital, interes, anyos)
