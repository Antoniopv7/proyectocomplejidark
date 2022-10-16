############################# algoritmo de seleccion

def seleccion(aList):
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


############################# algoritmo de insercion

############################# algoritmo de burbuja

def burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]


############################# algoritmo de burbuja

############################# algoritmo de quicksort

def quicksort(lista):
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
        return quicksort(izquierda)+centro+quicksort(derecha)
    else:
        return lista


############################# algoritmo de quicksort

############################# algoritmo de mergesort

def merge_sort(lista):
    if len(lista) < 2:
        return lista
    
    else:        
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

# Función merge
def merge(lista1, lista2):
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    result += lista1[i:]
    result += lista2[j:]

    return result


############################# algoritmo de mergesort

############################# algoritmo de heapsort




############################# algoritmo de heapsort