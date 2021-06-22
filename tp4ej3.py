################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def convertir_a_fahrrenheit(centigrados):
    far = (centigrados * 9.0 / 5.0 + 32)
    return far


def convertir_a_centigrados(fahrenheit):
    cen = ((fahrenheit - 32) * 5.0 / 9.0)
    return cen


if __name__ == "__main__":
    f = convertir_a_fahrrenheit(54)
    print(f)

    c = convertir_a_centigrados(30)
    print(c)
