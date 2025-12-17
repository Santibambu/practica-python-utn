# Ejercicio 1
for i in range (1, 11, 1):
    print(i)

# Ejercicio 2
for i in range (10, 0, -1):
     print(i)

# Ejercicio 3
Número = int(input("Porfavor, ingrese un número\n"))

for i in range (1, Número + 1, 1):
    print(i)

# Ejercicio 4
NúmeroMultiplicar = int(input("Porfavor, ingrese un número\n"))

for i in range (0, 11, 1):
    print(i * NúmeroMultiplicar)

# Ejercicio 5
Acumulador = 0
Contador = 0
Bandera0 = False

for i in range (10):
    NúmeroSuma = int(input("Porfavor, ingrese un número\n"))
    Acumulador += NúmeroSuma
    Contador += 1
    if NúmeroSuma == 0:
        print(f"La suma de todos los números ingresados es {Acumulador}")
        print(f"El promedio de todos los números ingresados es {Acumulador / Contador}")
        Bandera0 = True
        break

if Bandera0 == False:
    print(f"La suma de todos los números ingresados es {Acumulador}")
    print(f"El promedio de todos los números ingresados es {Acumulador / Contador}")

# Ejercicio 6
for i in range (1, 10):
    if i % 3 == 0:
        print(i)

# Ejercicio 7
for i in range (1, 50):
    if i % 2 == 0:
        print(i)

# Ejercicio 8
Pirámide = ""

NúmeroPirámide = int((input("Porfavor, ingrese un número\n")))

for i in range (1, NúmeroPirámide + 1):
    Pirámide += str(i)
    print(Pirámide)

# Ejercicio 9
AcumuladorDivisores = 0
DivisoresEncontrados = ""

NúmeroDividir = int(input("Porfavor, ingrese un número\n"))

for i in range (1, NúmeroDividir + 1):
    if NúmeroDividir % i == 0:
        AcumuladorDivisores += 1
        DivisoresEncontrados += (str(i) + ", ")

print(f"Se encontraron {AcumuladorDivisores} divisores para {NúmeroDividir}")
print(f"Aquellos divisores son: {DivisoresEncontrados[:-2]}")

# Ejercicio 10

DivisioresPrimo = 0
NoPrimo = False

NúmeroPrimo = int(input("Porfavor, ingrese un número\n"))

if NúmeroPrimo <= 0:
    print("El número ingresado no es primo")
    NoPrimo = True
else:
    for i in range (1, NúmeroPrimo + 1):
        if NúmeroPrimo % i == 0:
            DivisoresPrimo += 1

if NoPrimo == False:
    if DivisoresPrimo == 2:
        print("El número ingresado es primo")
    else:
        print("El número ingresado no es primo")

# Ejercicio 11

AcumuladorPrimos = 0
PrimosEncontrados = ""

BúsquedaPrimos = int(input("Porfavor, ingrese un número\n"))

for i in range (2, BúsquedaPrimos + 1):
    Divisores = 0
    for j in range (1, i + 1):
        if i % j == 0:
            Divisores += 1
    if Divisores == 2:
        AcumuladorPrimos += 1
        PrimosEncontrados += str(i) + ", "

print(f"Se encontraron {AcumuladorPrimos} números primos entre el 1 y el {BúsquedaPrimos}")
print(f"Aquellos números primos son: {PrimosEncontrados[:-2]}")