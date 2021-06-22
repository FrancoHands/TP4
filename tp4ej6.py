################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def minimo(lista_min):
    minval = lista_min[0]
    for i in range(0, len(lista_min)):
        if lista_min[i] < minval:
            minval = lista_min[i]
    return minval


def maximo(lista_max):
    maxval = lista_max[0]
    for i in range(0, len(lista_max)):
        if lista_max[i] > maxval:
            maxval = lista_max[i]
    return maxval


if __name__ == "__main__":
    lista = [7, 2, -5, 4, 20, -10, 1, 7]
    menor = minimo(lista)
    print(menor)
    mayor = maximo(lista)
    print(mayor)
