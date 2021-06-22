################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def factores_primos(numero):
    print(numero, " = ", end="")
    factor_primo = 2
    primer_factor = True
    while numero > 1:
        if numero % factor_primo == 0:
            if primer_factor:
                primer_factor = False
            else:
                print(" x ", end="")
            print(factor_primo, end="")
            numero //= factor_primo
        else:
            factor_primo += 1


if __name__ == '__main__':
    factores_primos(80)
