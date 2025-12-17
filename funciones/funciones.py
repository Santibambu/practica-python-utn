import random

# Ejercicio 1

def MostrarNúmero(Número):
    """Muestra por consola el número que recibe como parámetro"""
    print(Número)

MostrarNúmero(random.randint(1, 100))

# Ejercicio 2

def DevolverNúmero() -> int:
    """Solicita un número al usuario y lo devuelve"""
    Número = int((input("Porfavor, ingrese un número\n")))
    return(Número)

print(DevolverNúmero())

# Ejercicio 3

def VerificarPar(Número) -> bool:
    """
    Verifica si el número recibido es par
    Si es par, devuelve True; de lo contrario, devuelve False
    """
    if Número % 2 == 0:
        return True
    else:
        return False

print(VerificarPar(random.randint(1, 100)))

# Ejercicio 4

def MostrarNúmeroEnRango(Desde, Hasta) -> bool:
    """
    Solicita un número al usuario y lo muestra por consola
    Luego, verifica si ese número se encuentro dentro de un rango específico
    Si se encuentra dentro del rango, devuelve True; de lo contario, devuelve False
    """
    Número = int((input("Porfavor, ingrese un número\n")))
    print(Número)
    if Desde <= Número <= Hasta:
        return True
    else:
        return False

print(MostrarNúmeroEnRango(10, 100))

# Ejercicio 5

def Restar1 (Número1, Número2) -> int:
    """Resta los números que obtiene como parámetros y devuelve el resultado"""
    Resultado = Número1 - Número2
    return Resultado

print(Restar1(random.randint(1, 100), random.randint(1, 100)))

def Restar2() -> int:
    """
    Solicita dos números al usuario
    Los resta y devuelve el resultado
    """
    Número1 = int((input("Porfavor, ingrese un número\n")))
    Número2 = int((input("Porfavor, ingrese otro número\n")))
    Resultado = Número1 - Número2
    return Resultado

print(Restar2)

def Restar3(Número1, Número2):
    """Resta los números que obtiene como parámetros e imprime el resultado"""
    Resultado = Número1 - Número2
    print(Resultado)

Restar3(random.randint(1, 100), random.randint(1, 100))

def Restar4():
    """
    Solicita dos números al usuario
    Los resta e imprime el resultado
    """
    Número1 = int((input("Porfavor, ingrese un número\n")))
    Número2 = int((input("Porfavor, ingrese otro número\n")))
    Resultado = Número1 - Número2
    print(Resultado)

Restar4()

# Ejercicio 6

Número1 = MostrarNúmeroEnRango(10, 100)

def RealizarDescuento(Número):
    """Recibe un número como parámetro, le aplica un descuento del 10% e imprime el resultado"""
    Descuento = Número * .10
    Resultado = Número - Descuento
    print(Resultado)

RealizarDescuento(Número1)

# Ejercicio 7

def VerificarNúmero(Desde, Hasta) -> int:
    """
    Obtiene un rango de números
    Solicita un número al usuario y verifica que este dentro del rango que recibió como parámetros
    Devuelve el número validado
    """
    Número = int((input("Porfavor, ingrese un número\n")))
    while not (Desde <= Número <= Hasta):
        Número = int((input("El número ingresado no se encuentra del rango disponible. Porfavor, vuelva a ingresar un número\n")))
    return Número

Número1 = VerificarNúmero(10, 100)
Número2 = VerificarNúmero(10, 100)

def AsignarOperación() -> str:
    """Solicita un tipo de operación al usuario, la valida y la devuelve"""
    Operación = input("¿Qué tipo de operación desea realizar?\nS = Sumar\nR = Restar\n").upper()
    while Operación not in ["S", "R"]:
        Operación = input("El tipo de operación ingresado es erróneo. Vuelva a ingresar la operación deseada\nS = Sumar\nR = Restar").upper()
    return Operación

Operación = AsignarOperación()

def RealizarOperación(Número1, Número2):
    """
    Obtiene dos números como parámetros
    (Definido previamente) Si operación es S, realiza una suma entre los números recibidos e imprime el resultado
    (Definido previamente) Si operación es R, realiza una resta entre los números recibidos e imprime el resultado
    """
    if Operación == "S":
        Resultado = Número1 + Número2
        print(Resultado)
    else:
        Resultado = Número1 - Número2
        print(Resultado)

RealizarOperación(Número1, Número2)