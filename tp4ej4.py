################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def compara(numero, otro_numero):
    if numero == otro_numero:
        return 0
    elif numero < otro_numero:
        return -1
    else:
        return 1


if __name__ == "__main__":
    r = compara(15, 5)
    print(r)
