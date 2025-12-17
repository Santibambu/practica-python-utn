# Ejercicio 1

Contador = 0

while Contador != 10:
    Contador += 1
    print(Contador)

# Ejercicio 2

Contador = 11

while Contador != 1:
    Contador -= 1
    print(Contador)

# Ejercicio 3

Contador = 0
Acumulador = 0

while Contador != 10:
    Contador += 1
    Acumulador += Contador
print(Acumulador)

# Ejercicio 4

Contador = 0
Acumulador = 0

while Contador != 10:
    Contador += 1
    if Contador % 2 == 0:
        Acumulador += Contador
print(Acumulador)

# Ejercicio 5

Contador = 0
Acumulador = 0
Promedio = 0

while Contador != 5:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n"))
    print(f"La suma de los números ingresados hasta el momento es {Acumulador}")
    Promedio = Acumulador / Contador
    print(f"El promedio de los números ingresados hasta el momento es {Promedio}")

# Ejercicio 6

Ingreso = True
Contador = 0
Acumulador = 0
Promedio = 0

while Ingreso == True:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n")) 
    Promedio = Acumulador / Contador
    Respuesta = input("¿Le gustaría seguir agregando números? (S/N)\n").upper()
    if Respuesta == "S":
        Ingreso = True
    elif Respuesta == "N":
        Ingreso = False
print(f"La suma de los números ingresados es {Acumulador}")
print(f"El promedio de los números ingresados es {Promedio}")

# Ejercicio 7

Ingreso = True
SumaPositivos = 0
ProductoNegativos = 1

while Ingreso == True:
    Número = int(input("Porfavor, ingrese un número\n")) 
    if Número > 0:
        SumaPositivos += Número
    elif Número < 0:
        ProductoNegativos *= Número
    Respuesta = input("¿Le gustaría seguir agregando números? (S/N)\n").upper()
    if Respuesta == "S":
        Ingreso = True
    elif Respuesta == "N":
        Ingreso = False
print(f"La suma de los números positivos ingresados es {SumaPositivos}")
print(f"El producto de los números negativos ingresados es {ProductoNegativos}")

# Ejercicio 8

Contador = 0
NúmeroMáximo = float("-inf")
NúmeroMínimo = float("inf")

while Contador != 10:
    Contador += 1
    Número = int(input("Porfavor, ingrese un número\n"))
    if Número > NúmeroMáximo:
        NúmeroMáximo = Número
    if Número < NúmeroMínimo:
        NúmeroMínimo = Número
print(f"De los números ingresados, el mayor es {NúmeroMáximo}")
print(f"De los números ingresados, el menor es {NúmeroMínimo}")

# Ejercicio 9

Contador = 0
Acumulador = 0
Promedio = 0
Ingreso = True

while Contador != 4:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n"))
    Promedio = Acumulador / Contador

while Ingreso == True:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n")) 
    Promedio = Acumulador / Contador
    Respuesta = input("¿Le gustaría seguir agregando números? (S/N)\n").upper()
    if Respuesta == "S":
        Ingreso = True
    elif Respuesta == "N":
        Ingreso = False

print(f"La suma de los números ingresados es {Acumulador}")
print(f"El promedio de los números ingresados es {Promedio}")

# Ejercicio 10

Contador = 0
Acumulador = 0
Promedio = 0
Ingreso = True

while Contador != 4:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n"))
    Promedio = Acumulador / Contador

while Ingreso == True and Contador != 10:
    Contador += 1
    Acumulador += int(input("Porfavor, ingrese un número\n")) 
    Promedio = Acumulador / Contador
    if Contador == 10:
        break
    Respuesta = input("¿Le gustaría seguir agregando números? (S/N)\n").upper()
    if Respuesta == "S":
        Ingreso = True
    elif Respuesta == "N":
        Ingreso = False

print(f"La suma de los números ingresados es {Acumulador}")
print(f"El promedio de los números ingresados es {Promedio}")