import json

def ordenamiento_seleccion(lista):
    for n in range(len(lista) - 1 ,0, -1):
        posicion_maxima = 0

        for L in range(1, n + 1):
            if lista[1] > lista[posicion_maxima]:
                posicion_maxima = 1

        temp = lista[n]
        lista[n] = lista[posicion_maxima]
        lista[posicion_maxima] = temp          