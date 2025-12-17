# Ejercicio 1)
def crear_matriz_vocales(cadena:str) -> list:
    """
    Cuenta la cantidad de cada vocal en la cadena recibida.
    
    Parámetros:
        cadena (str): Cadena de caracteres a analizar.
    
    Devuelve:
        list: Matriz con las vocales y su cantidad correspondiente.
    """
    matriz_vocales = [["A", 0],
                      ["E", 0],
                      ["I", 0],
                      ["O", 0],
                      ["U", 0]]
    for i in range(len(cadena)):
        if cadena[i].upper() == "A":
            matriz_vocales[0][1] += 1
        elif cadena[i].upper() == "E":
            matriz_vocales[1][1] += 1
        elif cadena[i].upper() == "I":
            matriz_vocales[2][1] += 1
        elif cadena[i].upper() == "O":
            matriz_vocales[3][1] += 1
        elif cadena[i].upper() == "U":
            matriz_vocales[4][1] += 1
    return matriz_vocales

# Ejercicio 2)
def encontrar_caracter(cadena:str, caracter:str) -> int:
    """
    Busca la primera aparición de un carácter en la cadena (sin distinguir mayúsculas/minúsculas).
    
    Parámetros:
        cadena (str): Cadena donde buscar.
        caracter (str): Carácter a buscar (se compara en mayúsculas).
    
    Devuelve:
        int: Índice de la primera aparición o -1 si no se encuentra.
    """
    for i in range(len(cadena)):
        if cadena[i].upper() == caracter:
            resultado = i
            break
        else:
            resultado = -1
    return resultado

# Ejercicio 3)
def es_palíndromo(cadena:str) -> bool:
    """
    Verifica si la cadena es un palíndromo (sin distinguir mayúsculas/minúsculas).
    
    Parámetros:
        cadena (str): Cadena a verificar.
    
    Devuelve:
        bool: True si es palíndromo, False en caso contrario.
    """
    longitud = len(cadena)
    resultado = True
    
    for i in range(longitud // 2):
        if cadena[i].upper() != cadena[longitud - 1 - i].upper():
            resultado = False
            break
    return resultado

# Ejercicio 4)
def suprimir_caracteres_repetidos(cadena:str) -> str:
    """
    Elimina caracteres consecutivos repetidos en la cadena.
    
    Parámetros:
        cadena (str): Cadena a procesar.
    
    Devuelve:
        str: Cadena sin caracteres consecutivos repetidos.
    """
    caracteres_permitidos = cadena[0]  

    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i-1]:
            caracteres_permitidos += cadena[i]
    return caracteres_permitidos

# Ejercicio 5)
def suprimir_vocales(cadena:str) -> str:
    """
    Elimina todas las vocales de la cadena (sin distinguir mayúsculas/minúsculas).
    
    Parámetros:
        cadena (str): Cadena a procesar.
    
    Devuelve:
        str: Cadena sin vocales.
    """
    caracteres_permitidos = ""

    for i in range(len(cadena) - 1):
        if cadena[i].upper() not in ["A", "E", "I", "O", "U"]:
            caracteres_permitidos += cadena[i]
    return caracteres_permitidos

# Ejericio 6)
def contar_subcadenas(cadena:str, subcadena:str) -> int:
    """
    Cuenta cuántas veces aparece una subcadena dentro de una cadena.
    
    Parámetros:
        cadena (str): Cadena principal donde buscar.
        subcadena (str): Subcadena a contar.
    
    Devuelve:
        int: Cantidad de veces que aparece la subcadena.
    """
    contador = 0

    for i in range(len(cadena)):
        if cadena[i:i + len(subcadena)] == subcadena:
            contador += 1
    return contador