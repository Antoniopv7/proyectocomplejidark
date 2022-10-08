############################# algoritmo de seleccion

def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k                 
                
        swap(aList, least, i)
    return aList


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

print("Ordenamiento por Seleccion")
my_list = [5.76,4.7,25.3,4.6,32.4,55.3,52.3,7.6,7.3,86.7,43.5]
selectionSort(my_list)
print (my_list)

############################# algoritmo de seleccion

############################# algoritmo de insercion

#Declaracion de Funciones
def insercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j]
                A[j]=A[j-1]
                A[j-1]=aux
    return A

#Programa Principal
print("Ordenamiento por Insercion")
A=[6,5,3,1,8,7,2,4]
insercion(A)
print(A)

############################# algoritmo de insercion

############################# algoritmo de burbuja

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

print("Ordenamiento por Burbuja")
elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos)

############################# algoritmo de burbuja

############################# algoritmo de quicksort

miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
        return lista

print("Ordenamiento por quicksort")
print(miLista)
print(sort(miLista))

############################# algoritmo de quicksort

############################# algoritmo de mergesort

def merge_sort(lista):

    if len(lista) < 2:
        return lista

    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado

# Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

# Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result

# Prueba del algoritmo

print("Ordenamiento por mergesort")
lista = [31,3,88,1,4,2,42]

merge_sort_result = merge_sort(lista)
print(merge_sort_result)

############################# algoritmo de mergesort

############################# algoritmo de heapsort

import random

def heap_sort (heap): # Saque el nodo raíz e intercambie con el último bit, y continúe el proceso de ajuste del montón para los primeros nodos len-1.
    build_max_heap(heap)
    # El primer elemento de la lista ajustada es el elemento más grande de esta lista, cámbielo por el último elemento y luego ajuste recursivamente la lista restante al montón máximo
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)

# Prueba
if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    heap_sort(a)
    print(a)
    b = [random.randint(1,1000) for i in range(1000)]
    print(b)
    heap_sort(b)
    print(b)


############################# algoritmo de heapsort