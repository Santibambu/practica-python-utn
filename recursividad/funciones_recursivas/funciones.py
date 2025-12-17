# Ejercicio 1
def SumarNaturales(número: int) -> int:
    """
    Recibe un número como parámetro, que determinará la cantidad de números naturales desde 0 que se sumarán
    Si el número es igual o menor a 0, devuelve 0 (no es natural)
    De lo contrario, devuelve el número ingresado sumado a la llamada de la propia función, usando como parámetro el mismo número ingresado - 1
    """
    if número <= 0:
        return 0
    else:
        return número + SumarNaturales(número - 1)
    
# Ejercicio 2
def CalcularPotencia(base: int, exponente: int) -> int:
    """
    Recibe dos números como parámetros: el primero actuará como base para una potencia, y el segundo como el exponnete
    Si el exponente es 0, devuelve un error, ya que es imposible elevar un número
    Si en cambio el exponente es 0, devuelve 1
    Si en cambio el exponente es 1, devuelve la base
    Si no se cumplen ninguna de las condiciones anteriores, la función devuelve la base multiplicada por la llamada a sí misma con los argumentos de base y exponente - 1
    """
    if exponente < 0:
        raise ValueError("El exponente no puede ser menor que 0")
    elif exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * CalcularPotencia(base, exponente - 1)
        
# Ejercicio 3
def SumarDígitos(número: int) -> int:
    """
    Recibe un número como parámetro
    Si el número se encuentra entre -9 y 9, devuelve el número ingresado
    De lo contrario, crea dos variables:
    La primera es para almacenar el último dígito del número, que se crea al realizar la operación número % 10
    La segunda es para almacenar el resto del número sin el último dígito, que se crea al realizar la operación número // 10
    Finalmente, devuelve el último dígito del número sumado a la llamada de sí misma usando el resto del número como parámetro
    """
    if -10 < número < 10:
        return número
    else:
        ÚltimoDígito = número % 10
        RestoDelNúmero = número // 10
        return ÚltimoDígito + SumarDígitos(RestoDelNúmero)