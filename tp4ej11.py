################
# Franco Handsztok - @FrancoHands
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    longitud = len(texto)
    if longitud % 2 == 0:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2:]
    else:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2 + 1:]

    return izquierda == derecha[::-1]


if __name__ == "__main__":
    pal = es_palindromo("holaaloh")
    print(pal)
