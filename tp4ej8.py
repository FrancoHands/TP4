################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def ordenar_mayor_a_menor(uno, dos, tres):
    a = uno
    b = dos
    c = tres
    if b > a:
        aux = a
        a = b
        b = aux
    if c > b:
        aux = b
        b = c
        c = aux
    if b > a:
        aux = a
        a = b
        b = aux
    return a, b, c


def ordenar_menor_a_mayor(uno, dos, tres):
    a = uno
    b = dos
    c = tres
    if b < a:
        aux = a
        a = b
        b = aux
    if c < b:
        aux = b
        b = c
        c = aux
    if b < a:
        aux = a
        a = b
        b = aux
    return a, b, c


if __name__ == "__main__":
    res = ordenar_mayor_a_menor(3, 5, 1)
    print(res)
    res2 = ordenar_menor_a_mayor(3, 5, 1)
    print(res2)
