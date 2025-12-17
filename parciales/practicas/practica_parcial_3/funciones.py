def crear_matriz() -> list:
    matriz = [[5, 2, 3, 4],
              [5, 2, 7, 8],
              [2, 2, 3, 1],
              [1, 6, 7, 4]]
    return matriz

def verificar_columnas(matriz:list):
    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i])):
            if matriz[i][j] == matriz[i + 1][j] == matriz[i + 2][j]:
                resultado = matriz[i][j]
                break
            else:
                resultado = None
        return resultado