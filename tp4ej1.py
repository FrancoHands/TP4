################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def ingreso_entero():
    mensaje = "ingrese un numero:"
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
        print("su numero es: " + str(entero))
    except ValueError:
        print("ingreso incorrecto")
        ingreso_entero()


def entero_entre_2(minval=0, maxval=10):
    mensaje = "ingrese un numero entre " + str(minval) + " y " + str(maxval) + ":"
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
        print("su numero es: " + str(entero))
        if minval < entero < maxval:
            pass
        else:
            print("el numero esta fuera de rango")
    except ValueError:
        print("ingreso incorrecto")
        entero_entre_2(minval, maxval)


if __name__ == "__main__":
    ingreso_entero()
    entero_entre_2()
