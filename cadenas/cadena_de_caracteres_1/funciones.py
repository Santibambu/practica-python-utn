def encontrar_letra(letra:str, cadena:str) -> int:
    """
    Cuenta cuántas veces aparece una letra (ignorando mayúsculas/minúsculas) en una cadena.

    Parámetros:
        letra (str): La letra a buscar (se compara en mayúsculas).
        cadena (str): La cadena donde buscar la letra.

    Devuelve:
        int: El número de veces que la letra aparece en la cadena.
    """
    contador = 0
    for i in range(len(cadena)):
        if cadena[i].upper() == letra:
            contador += 1
    return contador

def dividir_cadena(cadena:str, desde:int, hasta:int) -> str:
    """
    Devuelve una subcadena de la cadena original entre los índices dados.

    Parámetros:
        cadena (str): La cadena original.
        desde (int): Índice inicial (incluido).
        hasta (int): Índice final (excluido).

    Devuelve:
        str: La subcadena que comienza en 'desde' y termina en 'hasta'. Si los índices no son válidos, imprime un mensaje y retorna None.
    """
    if not (0 <= desde < len(cadena) and 0 <= hasta <= len(cadena)):
        print("No se han encontrado índices para el rango ingresado.")
    else:
        return cadena[desde:hasta]
    
def char_at(cadena:str, num:int) -> str:
    """
    Devuelve el carácter en la posición indicada de la cadena.

    Parámetros:
        cadena (str): La cadena de la cual obtener el carácter.
        num (int): El índice del carácter a obtener.

    Devuelve:
        str: El carácter en la posición 'num'. Si el índice no es válido, imprime un mensaje y retorna None.
    """
    if not (0 <= num <= len(cadena) - 1):
        print("No se ha encontrado un índice para el número ingresado.")
    else:
        return cadena[num]