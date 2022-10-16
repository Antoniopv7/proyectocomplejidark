import libreria as li
import tkinter as tk
import random
from timeit import default_timer

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

7
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Ejecutgar Algoritmo de Ordenamiento por Seleccion: ', accion1),
        '2': ('Ejecutgar Algoritmo de Ordenamiento por Insercion: ', accion2),
        '3': ('Ejecutgar Algoritmo de Ordenamiento por Burbuja: ', accion3),
        '4': ('Ejecutgar Algoritmo de Ordenamiento por Quicksort: ', accion4),
        '5': ('Ejecutgar Algoritmo de Ordenamiento por Mergesort: ', accion5),
        '6': ('Ejecutgar Algoritmo de Ordenamiento por Heapsort: ', accion6),
        '7': ('Salir', salir)
    }

    generar_menu(opciones, '7')


def accion1():
    print('Has elegido la opción 1')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.seleccion(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')


def accion2():
    print('Has elegido la opción 2')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.insercion(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')


def accion3():
    print('Has elegido la opción 3')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.burbuja(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')


def accion4():
    print('Has elegido la opción 4')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    print(li.quicksort(res))
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')


def accion5():
    print('Has elegido la opción 5')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print(res)
    tInicial = default_timer()
    print(li.merge_sort(res))
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')   

def accion6():
    print('Has elegido la opción 6')
    a = input('Seleccione el rango de la Lista: ')
    res = [random.randrange(1, 50, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.heap_sort(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()