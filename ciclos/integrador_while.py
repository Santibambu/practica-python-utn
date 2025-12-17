Ingreso = True
Contador = 0
SumaNegativos = 0
SumaPositivos = 0
CantidadNegativos = 0
CantidadPositivos = 0
PromedioPositivos = 0
PositivoMayor = float("-inf")

while Ingreso == True:
    Contador += 1
    Número = int(input("Porfavor, ingrese un número\n"))
    if Número < 0:
        CantidadNegativos += 1
        SumaNegativos += Número
    elif Número > 0:
        CantidadPositivos += 1
        SumaPositivos += Número
        PromedioPositivos = SumaPositivos / CantidadPositivos
        if Número > PositivoMayor:
            PositivoMayor = Número
    Respuesta = input("¿Le gustaría seguir agregando números? (S/N)\n").upper()
    if Respuesta == "S":
        Ingreso = True
    elif Respuesta == "N":
        Ingreso = False

PorcentajeNegativos = (CantidadNegativos / Contador) * 100

print(f"La suma de todos los números negativos ingresados es {SumaNegativos}")
print(f"La suma de todos los números positivos ingresados es {SumaPositivos}")
print(f"La cantidad de números negativos ingresados es {CantidadNegativos}")
print(f"El promedio de los números positivos ingresados es {PromedioPositivos}")
print(f"De los números positivos ingresados, el mayor es {PositivoMayor}")
print(f"De todos los números ingresados, un {PorcentajeNegativos}% fueron negativos")