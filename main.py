import libreria as li
import random
from timeit import default_timer

####### Funcion para mostrar el menu y sus opciones
def mostrar_menu(opciones):
    print('Seleccione el Algoritmo de Ordenamiento que desea ejecutar:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

###### Funcion para leer las opciones
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

###### Funcion para ejecutar las opciones
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

###### Funcion para generar el menu asi como sus opciones y cual sera su opcion de salida
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

##### Funcion para crear el menu en base a las funciones acciones
def menu_principal():
    print('Bienvenido al Menu de Algoritmos de ordenamiento')
    opciones = {
        '1': ('Ejecutar Algoritmo de Ordenamiento por Seleccion: ', accion1),
        '2': ('Ejecutar Algoritmo de Ordenamiento por Insercion: ', accion2),
        '3': ('Ejecutar Algoritmo de Ordenamiento por Burbuja: ', accion3),
        '4': ('Ejecutar Algoritmo de Ordenamiento por Quicksort: ', accion4),
        '5': ('Ejecutar Algoritmo de Ordenamiento por Mergesort: ', accion5),
        '6': ('Ejecutar Algoritmo de Ordenamiento por Heapsort: ', accion6),
        '7': ('Salir', salir)
    }

    generar_menu(opciones, '7')

###### Estas funciones son las acciones en el menu
###### Funcion de la seleccion 1 en el menu
def accion1():
    print('Has elegido la opción 1')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.seleccion(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')

###### Funcion de la seleccion 2 en el menu
def accion2():
    print('Has elegido la opción 2')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.insercion(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')

###### Funcion de la seleccion 3 en el menu
def accion3():
    print('Has elegido la opción 3')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.burbuja(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')

###### Funcion de la seleccion 4 en el menu
def accion4():
    print('Has elegido la opción 4')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    print(li.quicksort(res))
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')

###### Funcion de la seleccion 5 en el menu
def accion5():
    print('Has elegido la opción 5')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 100, 1) for i in range(int(a))]
    print(res)
    tInicial = default_timer()
    print(li.merge_sort(res))
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')   

###### Funcion de la seleccion 6 en el menu
def accion6():
    print('Has elegido la opción 6')
    a = input('Seleccione el tamaño de la Lista que desea ordenar: ')
    res = [random.randrange(1, 50, 1) for i in range(int(a))]
    print (res)
    tInicial = default_timer()
    li.heapsort(res)
    print(res)
    tFinal = default_timer()
    ttotal_de_ejecucion_algoritmo = tFinal - tInicial
    print('El tiempo de ejecucion del algoritmo es de: '+ str(ttotal_de_ejecucion_algoritmo) + ' seg')

##### Funcion para salir del menu
def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()