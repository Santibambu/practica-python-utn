def calcular_promedio(lista:list, valor:int) -> bool: # Parámetros formales
    """
    Recibe una lista y un valor númerico, y devuelve True o False si el promedio de los números de la lista es mayor o menor al valor recibido
    Parámetros:
        lista (list): Una lista de números
        valor (int): Un valor númerico
    Devuelve:
        bool: True o False
    """
    contador = 0
    acumulador = 0
    for i in range(len(lista)):
        contador += 1
        acumulador += lista[i]
    if acumulador / contador > valor:
        resultado = True
    else:
        resultado = False
    return resultado