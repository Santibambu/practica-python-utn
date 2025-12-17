# Ejercicio 1
print("Bienvenido al centro de consultas de empleados\nA continuación, introduzca su nombre completo y su sueldo. Verificaremos si es apto para un aumento")
nombre = str(input("Ingrese su nombre completo.\n"))
sueldo = int(input("Ingrese su sueldo actual.\n"))
sueldoAumentado = sueldo + sueldo * .10
print(f"¡Felicidades, {nombre}! Usted es elegible para un aumento. Su sueldo ha incrementado un 10%, pasando de {sueldo} a {sueldoAumentado}")

#Ejercicio 2
edad = int(input("Ingrese su edad.\n"))
if edad >= 18:
    print("Es mayor de edad.")
elif edad <= 13:
    print("Es un niño.")
else:
    print("Es adolescente.")

#Ejercicio 3
print("¡Bienvenido a la Calculadora de Curiosidades!\nDeberá ingresar 5 números enteros, distintos de cero, y le diremos curiosades sobre ellos.\n")

pares = 0
impares = 0
parMayor = float("-inf")
sumaPositivos = 0
positivos = ""
productoNegativos = 1
negativos = ""

for i in range(5):
    número = int(input(f"Ingrese el {i+1}° número.\n"))

    while número == 0:
        print("El número no es distinto de cero. Vuelva a ingresar el número.")
        número = int(input(f"Ingrese el {i+1}° número.\n"))

    if número % 2 == 0:
        pares += 1
        if número > 0 and número > parMayor:
            parMayor = número
        elif número < 0 and número > parMayor:
            parMayor = número
    else:
        impares += 1
    
    if número > 0:
        sumaPositivos += número
        positivos = True
    else:
        productoNegativos *= número
        negativos = True
    
print("¡Gracias por ingresar los números!\nAquí están las curiosidades sobre los dígitos que nos ha proporcionado:")
print(f"Hay {pares} números pares y {impares} números impares")
if pares > 0:
    print(f"De los números pares, el mayor es {parMayor}")
if positivos == True:
    print(f"La suma de todos los números positivos iguala a {sumaPositivos}")
if negativos == True:
    print(f"El producto de todos los números negativos iguala a {productoNegativos}")
print("¡Muchas gracias por usar la Calculadora de Curiosidades!\nEsperemos que regrese pronto ;).")

# Ejercicio 4
print("Bienvenido a la aplicación de búsqueda de parejas más popular del país. Ingrese su edad y estado civil para continuar.\n")
edadParejas = int(input("Ingrese la edad.\n"))
estadoParejas = int(input("Ingrese el estado civil:\n1) Soltero\n2) Casado\n3) Separado\n4) Divorciado\n5) Viudo\n"))

match estadoParejas:
    case 1: estadoParejas = "Soltero"
    case 2: estadoParejas = "Casado"
    case 3: estadoParejas = "Separado"
    case 4: estadoParejas = "Divorciado"
    case 5: estadoParejas = "Viudo"
    case _: estadoParejas = "Indefinido"

while estadoParejas == "Indefinido":
    print("Tipo de estado civil no existente.\nVuelva a ingresar su estado civil\n")
    estadoParejas = int(input("1) Soltero\n2) Casado\n3) Separado\n4) Divorciado\n5) Viudo\n"))

if edadParejas < 18 and estadoParejas != "Soltero":
    print("Lo sentimos, pero es demasiado joven como para no estar soltero.\nSe le ha rechazado el acceso a la aplicación.")
else:
    print("¡Bienvenido a la aplicación!\nEsperemos que encuentre al amor de su vida ;).")

# Ejercicio 5

print("¡Bienvenido a Trivago, el mejor sitio de hotelería de todos!\nA continuación, ingrese el destino al que desea viajar y en qué estación le gustaría llegar allí.\n")
estación = int(input("Ingrese la estación durante la cual le gustaría viajar:\n1) Verano\n2) Otoño\n3) Invierno\n4) Primavera\n"))
destino = int(input("Ingrese el destino al cual le gustaría viajar:\n1) Bariloche\n2) Cataratas del Iguazú\n3) Mar del Plata\n4) Córdoba\n"))

precio = 15000

if estación == 1:
    if destino == 1:
        precio = precio - precio * .20
        print(f"El costo final de su viaje es de {precio} pesos")
    elif destino == 2 or destino == 4:
        precio = precio + precio * .10
        print(f"El costo final de su viaje es de {precio} pesos")
    elif destino == 3:
        precio = precio + precio *.20
        print(f"El costo final de su viaje es de {precio} pesos")
    else:
        print("Destino inexistente.\nVuelva a ingresar su destino.")
elif estación == 2 or estación == 4:
    if destino == 1 or destino == 2 or destino == 3:
        precio = precio + precio * .10
        print(f"El costo final de su viaje es de {precio} pesos")
    elif destino == 4:
        print(f"El costo final de su viaje es de {precio} pesos")
    else:
        print("Destino inexistente.\nVuelva a ingresar su destino.")
elif estación == 3:
    if destino == 1:
        precio = precio + precio * .20
        print(f"El costo final de su viaje es de {precio} pesos")
    elif destino == 2 or destino == 4:
        precio = precio - precio * .10
        print(f"El costo final de su viaje es de {precio} pesos")
    elif destino == 3:
        precio = precio - precio * .20
        print(f"El costo final de su viaje es de {precio} pesos")
    else:
        print("Destino inexistente.\nVuelva a ingresar su destino.")
else:
    print("Estación inexistente.\nVuelva a ingresar la estación.")