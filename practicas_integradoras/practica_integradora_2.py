IngresoDatos = True

JóvenesÉlitePlano = 0

EdadProdigio = float("inf")
NombreProdigio = ""
CategoríaProdigio = ""
Prodigio = False

CantidadExpertos = 0
JugadoresIngresados = 0

PromedioAvanzado = 0
JugadoresAvanzados = 0

PlanoPopular = 0
LiftadoPopular = 0
CortadoPopular = 0
SaquePopular = ""

while IngresoDatos == True:

    JugadoresIngresados += 1

    NombreJugador = input("Ingrese el nombre del jugador\n")

    EdadJugador = int(input("Ingrese la edad del jugador\n"))
    while EdadJugador < 18:
        EdadJugador = int(input("El jugador no puede tener menos de 18 años. Vuelva a ingresar la edad\n"))

    Puntos = int(input("Ingrese la cantidad de puntos\n"))
    while Puntos < 0 or Puntos > 60:
        Puntos = int(input("La cantidad de puntos no puede ser menor a 0 o mayor a 60. Vuelva a ingresar los puntos\n"))

    Victorias = int(input("Ingrese la cantidad de partidos ganados\n"))
    while Victorias < 0 or Victorias > 35:
        Victorias = int(input("La cantidad de partidos ganados no puede ser menos que 0 o mayor que 35. Vuelva a ingresar la cantidad de partidos ganados\n"))

    Saque = int(input("Ingrese el tipo de saque:\n1) Plano\n2) Liftado\n3) Cortado\n"))
    if Saque not in [1, 2, 3]:
        print("El saque no fue ingresado correctamente y no se tomará en cuenta para el cálculo de estadísticas\n")

    Categoría = int(input("Ingrese la categoría:\n1) Élite\n2) Experto\n3) Avanzado\n"))
    if Categoría not in [1, 2, 3]:
        print("La categoría no fue ingresada correctamente y no se tomará en cuenta para el cálculo de estadísticas\n")

    if Saque == 1 and Categoría == 1:
        PlanoPopular += 1
        if 19 <= EdadJugador <= 25:
            JóvenesÉlitePlano += 1
    elif Saque == 2 and Categoría == 1:
        LiftadoPopular += 1
    elif Saque == 3 and Categoría == 1:
        CortadoPopular += 1

    if EdadJugador < EdadProdigio and Puntos >= 50:
        EdadProdigio = EdadJugador
        NombreProdigio = NombreJugador
        Prodigio = True
        if Categoría == 1:
            CategoríaProdigio = "élite"
        elif Categoría == 2:
            CategoríaProdigio = "experta"
        elif Categoría == 3:
            CategoríaProdigio = "avanzada"

    if Categoría == 2:
        CantidadExpertos += 1
    elif Categoría == 3:
        PromedioAvanzado += EdadJugador
        JugadoresAvanzados += 1

    IngresoDatos = input("¿Le gustaría seguir agregando datos? (S/N)\n").upper()
    while IngresoDatos not in ["S", "N"]:
        IngresoDatos = input("Opción inválida.\n¿Le gustaría seguir agregando datos? (S/N)\n").upper()
    if IngresoDatos == "N":
        IngresoDatos = False
    else:
        IngresoDatos = True

PorcentajeExpertos = (CantidadExpertos / JugadoresIngresados) * 100

PromedioAvanzado = PromedioAvanzado / JugadoresAvanzados

if PlanoPopular > LiftadoPopular and PlanoPopular > CortadoPopular:
    SaquePopular = "plano"
elif LiftadoPopular > PlanoPopular and LiftadoPopular > CortadoPopular:
    SaquePopular = "liftado"
elif CortadoPopular > PlanoPopular and CortadoPopular > LiftadoPopular:
    SaquePopular = "cortado"

print(f"{JóvenesÉlitePlano} jugadores de la clase élite de entre 19 y 25 años utilizan el saque plano")

if Prodigio == True:
    print(f"¡Hubo un jugador prodigio! Con {EdadProdigio} años de edad, {NombreProdigio} de la categoría {CategoríaProdigio} logró acumular un total de puntos igual o mayor a 50 puntos")

print(f"El promedio de jugadores en categoría experta es de {PorcentajeExpertos}%")

print(f"El promedio de edad de los jugadores en categoría avanzada es de {PromedioAvanzado} años")

print(f"El saque más utilizado por los jugadores de clasificación de élite es el {SaquePopular}")