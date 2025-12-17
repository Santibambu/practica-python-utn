# Juego "Radar del Tesoro"
MapaTesoro = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

FilaTesoro = 0
ColumnaTesoro = 0
for f in range(len(MapaTesoro)):
    for c in range(len(MapaTesoro[f])):
        if MapaTesoro[f][c] == 1:
            FilaTesoro = f
            ColumnaTesoro = c

def VerificarTesoro(mapa: list, x: int, y: int) -> int:
        """
        Verifica las coordenadas que ingresó el usuario para encontrar el tesoro dentro del mapa
        Si lo encontró, devuelve 0
        De lo contario, devuelve otro número

        Parámetros:
        mapa:list = Una lista que contiene dígitos binarios
        x: int = un entero que se usará como coordenada de fila
        x: int = un entero que se usará como coordenada de columna
        """
        if mapa[CoordenadaFila][CoordenadaColumna] == 1:
            Resultado = 0
        else:
            Manhattan = (x - FilaTesoro) + (y - ColumnaTesoro)
            Resultado = abs(Manhattan)
        if Resultado == 0:
            print("\n¡Encontraste el tesoro!\n")
        else:
            print(f"\nFallaste. El tesoro está a {Resultado} casilleros de distancia.\n" )
        return Resultado

while True:
    try:
        CoordenadaFila = int(input("Porfavor, ingrese la coordenada de una fila (desde 0 hasta 4)\n"))
        if CoordenadaFila < 0 or CoordenadaFila > 4:
            raise ValueError("la coordenada de la fila no puede ser ni menor a 0 ni mayor a 4")
        CoordenadaColumna = int(input("Porfavor, ingrese la coordenada de una columna (desde 0 hasta 4)\n"))
        if CoordenadaColumna < 0 or CoordenadaColumna > 4:
            raise ValueError("la coordenada de la columna no puede ser ni menor a 0 ni mayor a 4")
        if VerificarTesoro(MapaTesoro, CoordenadaFila, CoordenadaColumna) != 0:
            Continuar = input("No ha encontrado el tesoro. ¿Desea continuar jugando? (S/N)\n").upper()
            if Continuar not in ["S", "N"]:
                print("La opción ingresada es inválida. Vuelva a iniciar el programa.\n")
            elif Continuar == "N":
                print("Ha decidido dejar de jugar.\n")
                break
        else:
            break
    except ValueError as e:
        print(f"Error: {e}\n")