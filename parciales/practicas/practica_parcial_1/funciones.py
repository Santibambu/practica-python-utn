Tablero = [[0, 0, 1, 0, 0],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 1, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 1]]

def Disparar():
    BarcosHundidos = 0

    while True:
        try:
            CoordenadaFila = int(input("Porfavor, ingrese la coordenada de una fila (Desde 0 hasta 4)\n"))
            if CoordenadaFila <0 or CoordenadaFila > 4:
                raise ValueError("la coordenada de la fila no puede ser menor que 0 o mayor que 4")
            CoordenadaColumna = int(input("Porfavor, ingrese la coordenada de una columna (Desde 0 hasta 4)\n"))
            if CoordenadaColumna <0 or CoordenadaColumna > 4:
                raise ValueError("la coordenada de la columna no puede ser menor que 0 o mayor que 4")
            if VerificarCoordenadas(Tablero, CoordenadaFila, CoordenadaColumna) == True:
                BarcosHundidos += 1
            Elección = input("¿Desea ingresar otras coordenadas? (S/N)\n").upper()
            if Elección not in ["S", "N"]:
                raise ValueError("la opción elegida debe ser S o N")
            elif Elección == "N":
                print(f"Hundiste {BarcosHundidos} barcos en total")
                break
        except ValueError as e:
            print(f"Error: {e}\n")

def VerificarCoordenadas(tablero:list, x:int, y:int) -> bool:
        if tablero[x][y] == 0:
            print("Agua")
            Resultado = False
        elif tablero[x][y] == 1:
            print("Hundido")
            Resultado = True
        return Resultado