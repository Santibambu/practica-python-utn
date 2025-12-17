def mostrar_menú_de_opciones():
    """
    Muestra un menú de opciones al usuario y ejecuta acciones según la opción elegida.
    Parámetros:
        Ninguno.
    """
    while True:
        try:
            opción_elegida = int(input("\nBienvenido a la base de datos del departamento de ventas. Elija la opción que le gustaría realizar:\n1) Mostrar la lista de productos y la matriz de ventas.\n2) Ordenar los productos de mayor a menor según sus ventas totales anuales (suma de los trimestres).\n3) Buscar un producto por nombre y mostrar sus ventas.\n4) Buscar un valor de venta dentro de la matriz y mostrar a qué producto y trimestre pertenece.\n5) Cerrar sesión.\n"))
            if opción_elegida == 1:
                imprimir_planilla(productos, ventas, total_ventas)
            elif opción_elegida == 2:
                lista_ordenada = ordenar_mayor_menor_listas_paralelas(total_ventas, productos)
                imprimir_listas_paralelas(lista_ordenada, productos)
            elif opción_elegida == 3:
                buscar_elemento_e_imprimir_matriz_paralela(productos, ventas)
            elif opción_elegida == 4:
                buscar_elemento_e_imprimir_elementos_paralelos(ventas, productos)
            elif opción_elegida == 5:
                print("\nCerrando sesión...")
                break
            else:
                raise ValueError
        except ValueError:
            print("\nLa opción ingresada no es válida. Vuelva a intentarlo.")

def sumar_filas_matriz(matriz:list) -> list:
    """
    Calcula la suma de los elementos de cada fila de una matriz.
    Parámetros:
        matriz (list): Matriz de números a procesar.
    Devuelve:
        list: Lista con la suma de cada fila de la matriz.
    """
    suma_total = []
    for i in range(len(matriz)):
        suma_total.append(sum(matriz[i]))
    return suma_total

def imprimir_planilla(lista1:list, matriz:list, lista2:list):
    """
    Imprime una planilla con los productos, sus ventas trimestrales y el total anual.
    Parámetros:
        lista1 (list): Lista de nombres de productos.
        matriz (list): Matriz de ventas trimestrales.
        lista2 (list): Lista de totales anuales por producto.
    """
    print(f"\nVentas trimestrales (en miles de $):\nProducto | T1  | T2  | T3  | Total\n-----------------------------------")
    for i in range(len(lista1)):
        elemento_lista1 = lista1[i]
        elemento_matriz = matriz[i]
        elemento_lista2 = lista2[i]

        print(f"{elemento_lista1:>8} | {elemento_matriz[0]:>3} | {elemento_matriz[1]:>3} | {elemento_matriz[2]:>3} | {elemento_lista2:>5}")

def ordenar_mayor_menor_listas_paralelas(lista1:list, lista2:int) -> list:
    """
    Ordena una lista utilizando el método de burbujeo (bubble sort).
    Parámetros:
        lista (list): Lista a ordenar.
    Devuelve:
        list: Lista ordenada de mayor a menor.
    """
    for i in range(len(lista1) - 1):
        for j in range(i + 1, len(lista1)):
            if lista1[i] < lista1[j]:
                aux1 = lista1[i]
                aux2 = lista2[i]
                lista1[i] = lista1[j]
                lista2[i] = lista2[j]
                lista1[j] = aux1
                lista2[j] = aux2
    return lista1

def imprimir_listas_paralelas(lista1:list, lista2:list):
    """
    Imprime dos listas en paralelo, mostrando productos y sus ventas totales anuales ordenados de mayor a menor.
    Parámetros:
        lista1 (list): Lista de ventas totales anuales.
        lista2 (list): Lista de nombres de productos.
    """
    print("\nAquí está la lista de productos, ordenados de mayor a menor según la cantidad de ventas totales anuales")
    for i in range(len(lista1)):
        print(f"{lista2[i]} ({lista1[i]} Miles de Dólares)")


def buscar_elemento_e_imprimir_matriz_paralela(lista:list, matriz:list):
    """
    Busca un producto por nombre y muestra sus ventas trimestrales.
    Parámetros:
        lista (list): Lista de nombres de productos.
        matriz (list): Matriz de ventas trimestrales.
    """
    elemento_encontrado = False
    while elemento_encontrado == False:
        búsqueda = input(f"Ingrese el nombre del producto cuyas ventas desea analizar (si no se acuerda de la lista de productos, puede ejecutar la primer opción del menú)\n").upper()
        for i in range(len(lista)):
            elemento_matriz = matriz[i]
            if búsqueda == lista[i]:
                elemento_encontrado = True
                print(f"\nLas ventas de {búsqueda}, en miles de dólares, son: {elemento_matriz[0]} (T1), {elemento_matriz[1]} (T2), {elemento_matriz[2]} (T3)")
                break
        if elemento_encontrado == False:
            print("\nNo se ha encontrado ningún producto con ese nombre. Vuelva a intentarlo.\n")


def buscar_elemento_e_imprimir_elementos_paralelos(matriz:list, lista:list):
    """
    Busca un valor de venta en la matriz y muestra a qué producto y trimestre pertenece.
    Parámetros:
        matriz (list): Matriz de ventas trimestrales.
        lista (list): Lista de nombres de productos.
    """
    elemento_encontrado = False
    while elemento_encontrado == False:
        try:
            búsqueda = int(input("Ingrese el valor de venta cuyo origen desea analizar (si no se acuerda de la lista de valores de venta, puede ejcutar la primer opción del menú)\n"))
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if búsqueda == matriz[i][j]:
                        elemento_encontrado = True
                        if j == 0:
                            elemento = "Trimestre 1"
                        elif j == 1:
                            elemento = "Trimestre 2"
                        elif j == 2:
                            elemento = "Trimestre 3"
                        print(f"\nSe generaron {búsqueda} miles de dólares al vender {lista[i]} en el {elemento}")
            if elemento_encontrado == False:
               raise ValueError
        except ValueError:
            print("\nNo se ha encontrado ningún valor de venta con esa referencia. Vuelva a intentarlo.\n")

productos = ["A", "B", "C"]
ventas = [[50, 60, 70], # A
          [80, 55, 45], # B
          [40, 65, 75]] # C
total_ventas = sumar_filas_matriz(ventas)