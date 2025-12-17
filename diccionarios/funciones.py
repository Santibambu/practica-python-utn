from Estudiantes import *
def mostrar_menú_de_opciones():
    """
    Muestra un menú de opciones al usuario y ejecuta acciones según la opción elegida.
    Parámetros:
        Ninguno.
    """
    while True:
        try:
            opción_elegida = int(input("\nBienvenido. Elija la opción que le gustaría realizar:\n1) Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad\n2) Obtener el promedio de notas para cada estudiante\n3) Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de \"Ingenieria en Informatica\"\n4) Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido\n5) Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido\n6) Listar nombre y apellido de los alumnos que forman el grupo \"Club de Informática\" con sus respectivos promedios\n7) Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.\n8) Salir\n"))
            if opción_elegida == 1:
                ordenar_diccionarios_burbujeo(estudiantes, ["apellido", "nombre"])
                for estudiante in estudiantes:
                    print(f"\nLegajo: {estudiante["legajo"]}\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}\nEdad:{estudiante["edad"]}")
            elif opción_elegida == 2:
                promedios = promediar_elemento_listas_diccionarios(estudiantes, "notas")
                for estudiante, promedio in zip(estudiantes, promedios):
                    print(f"\nNombre: {estudiante["nombre"]}\nNotas: {estudiante["notas"]}\nPromedio: {promedio:.2f}")
            elif opción_elegida == 3:
                datos_programa = listar_datos_programa_informática(estudiantes, "programa", "nombre")
                for estudiante in datos_programa:
                    print(f"\nLegajo: {estudiante["legajo"]}\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}\nEdad:{estudiante["edad"]}")
            elif opción_elegida == 4:
                promedio = promediar_elemento_diccionarios(estudiantes, "edad")
                print(f"\nEl promedio de edad de todos los estudiantes es de {promedio} años.\nA continuación, una lista de cada estudiante con su edad.")
                for estudiante in estudiantes:
                    print(f"\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}\nEdad: {estudiante["edad"]}")
            elif opción_elegida == 5:
                promedios = promediar_elemento_listas_diccionarios(estudiantes, "notas")
                promedio_mayor = encontrar_promedio_mayor(promedios)
                print(f"\nEl mayor promedio de la universidad es de {promedio_mayor:.2f} puntos\nA continuación, una lista de cada estudiante con dicho promedio.")
                for estudiante, promedio in zip(estudiantes, promedios):
                    if promedio == promedio_mayor:
                        print(f"\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}")
            elif opción_elegida == 6:
                promedios = promediar_elemento_listas_diccionarios(estudiantes, "notas")
                datos_club = listar_datos_club_informática(estudiantes, "grupos", "nombre")
                for estudiante, promedio in zip(datos_club, promedios):
                    print(f"\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}\nPromedio: {promedio:.2f}")
            elif opción_elegida == 7:
                edad_menor = encontrar_edad_menor(estudiantes, "edad")
                print(f"\nLos estudiantes más jóvenes de la universidad tienen {edad_menor} años. A continuación, una lista con los datos de los estudiantes más jóvenes.")
                for estudiante in estudiantes:
                    if estudiante["edad"] == edad_menor:
                        print(f"\nLegajo: {estudiante["legajo"]}\nNombre: {estudiante["nombre"]}\nApellido: {estudiante["apellido"]}\nPrograma:{estudiante["programa"]}")
            elif opción_elegida == 8:
                print("\nCerrando sesión...\n")
                break
            else:
                raise ValueError
        except ValueError:
            print("\nLa opción ingresada no es válida. Vuelva a intentarlo.")

def ordenar_diccionarios_burbujeo(elementos: list, claves: list) -> list:
    """
    Ordena una lista de diccionarios utilizando el método de burbujeo (bubble sort),
    según una o más claves en orden de prioridad.
    
    Parámetros:
        elementos (list): Lista de diccionarios a ordenar.
        claves (list): Lista de claves por las que se ordenará en orden de prioridad.
    
    Devuelve:
        list: Lista ordenada de menor a mayor según las claves dadas.
    """
    for i in range(len(elementos) - 1):
        for j in range(i + 1, len(elementos)):
            ordenar = False
            for clave in claves:
                if elementos[i][clave] > elementos[j][clave]:
                    ordenar = True
                    break
                elif elementos[i][clave] < elementos[j][clave]:
                    break
            if ordenar:
                aux = elementos[i]
                elementos[i] = elementos[j]
                elementos[j] = aux
    return elementos

def promediar_elemento_listas_diccionarios(elementos:list, clave:str) -> list:
    """
    Calcula el promedio de los valores de una lista contenida en cada diccionario de una lista.
    
    Parámetros:
        elementos (list): Lista de diccionarios.
        clave (str): Clave cuyo valor es una lista de números a promediar.
    
    Devuelve:
        list: Lista de promedios para cada diccionario.
    """
    promedios = []
    for diccionario in elementos:
        números = diccionario[clave]
        acumulador = 0
        contador = 0

        for valor in números:
            acumulador += valor
            contador += 1
        promedio = acumulador / contador
        promedios.append(promedio)
    return promedios

def listar_datos_programa_informática(elementos:list, clave_primaria:str, clave_secundaria:str) -> list:
    """
    Filtra los estudiantes que cursan el programa de "Ingenieria en Informatica".
    
    Parámetros:
        elementos (list): Lista de diccionarios de estudiantes.
        clave_primaria (str): Clave para acceder al subdiccionario del programa.
        clave_secundaria (str): Clave para acceder al nombre del programa.
    
    Devuelve:
        list: Lista de estudiantes que cursan "Ingenieria en Informatica".
    """
    datos_programa_informática = []
    for estudiante in elementos:
        if estudiante[clave_primaria][clave_secundaria] == "Ingenieria en Informatica":
            datos_programa_informática.append(estudiante)
    return datos_programa_informática

def promediar_elemento_diccionarios(elementos:list, clave:str) -> list:
    """
    Calcula el promedio de los valores asociados a una clave en una lista de diccionarios.
    
    Parámetros:
        elementos (list): Lista de diccionarios.
        clave (str): Clave cuyos valores se promediarán.
    
    Devuelve:
        float: Promedio de los valores encontrados.
    """
    acumulador = 0
    contador = 0
    promedio = 0
    for estudiante in elementos:
        acumulador += estudiante[clave]
        contador += 1
        promedio = acumulador / contador
    return promedio

def encontrar_promedio_mayor(elementos:list) -> float:
    """
    Encuentra el valor máximo en una lista de promedios.
    
    Parámetros:
        elementos (list): Lista de promedios (números).
    
    Devuelve:
        float: El mayor promedio encontrado.
    """
    promedio_mayor = float("-inf")
    for promedio in elementos:
        if promedio > promedio_mayor:
            promedio_mayor = promedio
    return promedio_mayor

def listar_datos_club_informática(elementos:list, clave_primaria:str, clave_secundaria:str) -> list:
    """
    Filtra los estudiantes que pertenecen al grupo "Club de Informatica".
    
    Parámetros:
        elementos (list): Lista de diccionarios de estudiantes.
        clave_primaria (str): Clave para acceder a la lista de grupos.
        clave_secundaria (str): Clave para acceder al nombre del grupo.
    
    Devuelve:
        list: Lista de estudiantes que pertenecen al "Club de Informatica".
    """
    datos_club_informática = []
    for estudiante in elementos:
        try:
            grupos = estudiante[clave_primaria]
            for grupo in grupos:
                nombre_grupo = grupo[clave_secundaria]
                if nombre_grupo == "Club de Informatica":
                    datos_club_informática.append(estudiante)
                    break
        except KeyError:
            pass
    return datos_club_informática

def encontrar_edad_menor(elementos:list, clave:str) -> int:
    """
    Encuentra la menor edad entre los estudiantes.
    
    Parámetros:
        elementos (list): Lista de diccionarios de estudiantes.
        clave (str): Clave para acceder a la edad de cada estudiante.
    
    Devuelve:
        int: La menor edad encontrada.
    """
    edad_menor = float("inf")
    for estudiante in elementos:
        edad = estudiante[clave]
        if edad < edad_menor:
            edad_menor = edad
    return edad_menor