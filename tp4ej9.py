################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


def app():
    numero = int(input('Escribe un numero: '))
    resultado = es_primo(numero)

    if resultado is True:
        print('El numero es primo')
    else:
        print('El numero no es primo')


if __name__ == '__main__':
    app()
