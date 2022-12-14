############################# algoritmo de seleccion

def seleccion(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k                 
                
        swap(aList, least, i)
    return aList

#### Funcion para cambiar posiciones en la lista
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


############################# algoritmo de seleccion

############################# algoritmo de insercion

#Declaracion de Funciones
def insercion(X):
    for i in range(len(X)):
        for j in range(i,0,-1):
            if(X[j-1] > X[j]):
                aux=X[j]
                X[j]=X[j-1]
                X[j-1]=aux
    return X


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

# Funci??n merge
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

# devuelve el hijo izquierdo de `A[i]`
def LEFT(i):
    return 2*i + 1


# devuelve el hijo derecho de `A[i]`
def RIGHT(i):
    return 2*i + 2


# Funci??n de utilidad para intercambiar dos ??ndices en una lista
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Algoritmo de heapify-down recursivo. El nodo en el ??ndice `i` y
# sus dos hijos directos viola la propiedad del heap
def heapify(A, i, size):

    # obtener el hijo izquierdo y derecho del nodo en el ??ndice `i`
    left = LEFT(i)
    right = RIGHT(i) 
    largest = i

    # compara `A[i]` con su hijo izquierdo y derecho
    # y encuentre el valor m??s grande
    if left < size and A[left] > A[i]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    # Permuta # con hijo de mayor valor y
    # call heapify-down sobre el ni??o
    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, size)


# Funci??n para eliminar un elemento con la prioridad m??s alta (presente en la ra??z)
def pop(A, size):

    # si el heap no tiene elementos
    if size <= 0:
        return -1

    top = A[0]

    # reemplaza la ra??z del heap con el ??ltimo elemento
    # de la lista
    A[0] = A[size - 1]
    # Llamada # heapify-down en el nodo ra??z
    heapify(A, 0, size - 1)

    return top


# Funci??n para realizar heapsort en una lista `A` de tama??o `n`
def heapsort(A):

    # crea una cola de prioridad e inicial??zala seg??n la lista dada
    n = len(A)

    # Build-heap: Llame a heapify a partir del ??ltimo interno
    # Nodo # hasta el nodo ra??z
    i = (n - 2) // 2
    while i >= 0:
        heapify(A, i, n)
        i = i - 1

    # salta repetidamente del heap hasta que se vac??a
    while n:
        A[n - 1] = pop(A, n)
        n = n - 1
        

############################# algoritmo de heapsort