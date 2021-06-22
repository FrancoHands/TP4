################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def suma_lenta(numero, otro_numero):
    total = numero
    signo = int(otro_numero / abs(otro_numero))
    for i in range(0, abs(otro_numero)):
        total = total + signo
        print(total)
    return total


if __name__ == "__main__":
    suma_lenta(50, 20)
