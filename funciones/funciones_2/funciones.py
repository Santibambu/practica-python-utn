# Ejercicio 1
def CalcularÁreaRectángulo(base, altura) -> int:
    """
    Recibe la base y la altura de un rectángulo como parámetros
    Calcula el área de la forma geométrica
    Devuelve el resultado de la operación
    """
    Área = base * altura
    return Área

# Ejercicio 2
def CalcularÁreaCírculo(radio) -> float:
    """
    Recibe el radio de un círculo como parámetro
    Calcula el área de la forma geométrica
    Devuelve el resultado de la operación
    """
    Área = 3.14 * (radio ** 2)
    return Área

# Ejercicio 3
def VerificarYMostrarResto(número):
    """
    Recibe un número como parámetro
    Si el resto de la división de dicho número con 2 fuese 0, imprime un mensaje afirmando que es par
    De lo contrario, imprime un mensaje afirmando que es impar
    """
    if número % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

# Ejercicio 4
def VerificarYDevolverResto(número) -> bool:
    """
    Recibe un número como parámetro
    Si el resto de la división de dicho número con 2 fuese 0, devuelve True
    De lo contrario, devuelve False
    """
    if número % 2 == 0:
        return True
    else:
        return False
    
# Ejercicio 5
def DevolverNúmeroMayor(número1, número2, número3) -> int:
    """
    Recibe tres números como parámetros
    Designa al primer número recibido como el mayor
    Verifica si el segundo número recibido es mayor al número máximo registrado 
    De ser esto cierto, el segundo número pasa a ser el mayor; en caso contrario, no sucede nada
    Luego, verifica si el tercer número recibido es mayor al al número máximo registrado
    De ser esto cierto, el tercer número pasa a ser el mayor; en caso contrario, no sucede nada
    Devuelve el mayor de los tres números
    """
    NúmeroMayor = número1
    if número2 > NúmeroMayor:
        NúmeroMayor = número2
    if número3 > NúmeroMayor:
        NúmeroMayor = número3
    return NúmeroMayor

# Ejercicio 6
def CalcularPotencia(número, potencia) -> int:
    """
    Recibe dos números como parámetros
    El segundo número actúa como potencia del primero
    Devuelve el resultado de la operación
    """
    Resultado = número ** potencia
    return Resultado

# Ejercicio 7
def VerificarPrimo(número) -> bool:
    """
    Recibe un número como parámetro
    Verifica si el número es menor o igual que 1
    De ser así, devuelve False
    Verifica si el número es igual o menor a 3
    De ser así, devuelve True
    Verifica si al dividir el número por 2 o por 3 el resto da 0
    De ser así, devuelve False
    Inicializa una variable de iteración en 5
    Inicia un bucle while que itera mientras i * i sea menor o igual al número ingresado
    Verifica si al dividir el número por i o por i + 2 el resto es 0
    De ser así, devuelve False
    Incrementa la variable de iteración en 6
    Si el bucle finaliza, devuelve True
    """
    if número <= 1:
        return False
    if número <= 3:
        return True
    if número % 2 == 0 or número % 3 == 0:
        return False
    i = 5
    while i * i <= número:
        if número % i == 0 or número % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejercicio 8
def BuscarPrimos(número) -> int:
    """
    Recibe un número como parámetro
    Inicializa una variable que registrará la cantidad de números primos encontrados
    Inicia un bucle for que itera desde el 1 hasta el número ingresado
    Inicaliza una variable que registrará la cantida de divisores encontrados para un número
    Inicia otro bucle for que itera por cada iteración del primer bucle hasta que este finalice
    Verifica si al dividir la primera iteración con la segunda el resto es 0
    De ser así, suma 1 a la cantidad de divisores encontrados
    Verifica si la cantidad de divisores encontrados es 2
    De ser así, suma 1 a la cantidad de números primos encontrados
    Devuelve la cantidad de números primos encontrados
    """
    AcumuladorPrimos = 0
    for i in range (1, número + 1):
        Divisores = 0
        for j in range (1, i + 1):
            if i % j == 0:
                Divisores += 1
        if Divisores == 2:
            AcumuladorPrimos += 1
    return AcumuladorPrimos

# Ejercicio 9
def ImprimirTabla(número, inicio = 1, fin = 10):
    """
    Recibe tres número como parámetros: el primero definirá la tabla de multiplicación, mientras que los otros dos definirán el rango de números a multiplicar
    Inicia un bucle for que itera por el rango de los números ingresados como parámetros
    Cada vez que itera, imprime el resultado de la iteración por el primer número ingresado como parámetro
    """
    for i in range(inicio, fin + 1):
        print(i * número)

# Ejercicio 10
def SolicitarEntero() -> int:
    """
    No recibe parámetros
    Le pide al usuario que ingrese un número entero
    Mientras el número ingresado no sea un entero positivo, el input se repetirá en bucle hasta cumplir la condición
    Devuelve el número entero ingresado
    """
    Ingreso = (input("Porfavor, ingrese un número entero\n"))
    while not Ingreso.isdigit():
        Ingreso = (input("El número ingresado es inválido. Porfavor, vuelva a ingresar un número entero\n"))
    return int(Ingreso)

# Ejercicio 11
def SolicitarFlotante() -> float:
    """
    No recibe parámetros
    Le pide al usuario que ingrese un número flotante
    Mientras el número ingresado no sea apto para convertirse a flotante (tiene más de un punto, más de una coma o no es un dígito) el input se repetirá en bucle hasta cumplir la condición
    Devuelve el número flotante ingresado
    """
    Ingreso = (input("Porfavor, ingrese un número flotante\n"))
    while not Ingreso.replace(".", "", 1).replace("-", "", 1).isdigit() or Ingreso.count(".") > 1:
        Ingreso = (input("El número ingresado es inválido. Porfavor, vuelva a ingresar un número flotante\n"))
    return float(Ingreso)

# Ejercicio 12
def SolicitarCadena() -> str:
    Ingreso = (input("Porfavor, ingrese una cadena de caracteres\n"))
    while Ingreso.isdigit():
        Ingreso = (input("La cadena ingresada es inválida. Porfavor, vuelva a ingresar una cadena de caracteres\n"))
    return Ingreso