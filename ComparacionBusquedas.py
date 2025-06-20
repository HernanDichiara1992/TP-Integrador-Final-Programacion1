import time
import random

# ------------------------------
# Búsqueda binaria (iterativa)
# ------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ------------------------------
# Búsqueda lineal
# ------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ------------------------------
# Función que compara ambos algoritmos
# ------------------------------
def comparar_busquedas(tamano_lista):
    print(f"🔎 Prueba con {tamano_lista} elementos:")

    # Generar una lista de valores únicos aleatorios
    lista_original = random.sample(range(1, tamano_lista * 10), tamano_lista)
    target = lista_original[tamano_lista // 2]  # Valor garantizado en la lista

    # Ordenar la lista para aplicar búsqueda binaria
    lista_ordenada = lista_original.copy()
    lista_ordenada.sort()

    # Medir tiempo de búsqueda binaria
    start_time = time.time()
    pos_binaria = binary_search(lista_ordenada, target)
    end_time = time.time()
    tiempo_binaria = end_time - start_time
    print(f"Búsqueda binaria → posición {pos_binaria}, tiempo: {tiempo_binaria:.6f} segundos")

    # Medir tiempo de búsqueda lineal
    start_time = time.time()
    pos_lineal = linear_search(lista_original, target)
    end_time = time.time()
    tiempo_lineal = end_time - start_time
    print(f"Búsqueda lineal  → posición {pos_lineal}, tiempo: {tiempo_lineal:.6f} segundos")

    # Línea separadora
    print("-" * 60)

# ------------------------------
# Pruebas con distintos tamaños
# ------------------------------
if __name__ == "__main__":
    comparar_busquedas(1000)
    comparar_busquedas(10000)
    comparar_busquedas(100000)
    comparar_busquedas(1000000)