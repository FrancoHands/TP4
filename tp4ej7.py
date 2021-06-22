################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def division_lenta(dividendo, divisor):
    resto = dividendo
    cosiente = 0
    fin = False
    while not fin:
        if (resto - divisor) >= 0:
            resto = resto - divisor
            cosiente = cosiente + 1
        else:
            fin = True
    return cosiente, resto


if __name__ == "__main__":
    res = division_lenta(100, 6)
    print(res)
