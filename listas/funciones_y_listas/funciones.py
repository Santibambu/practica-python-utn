import random

# Ejercicio 1
def PedirListaNombres () -> list:
    """
    No recibe parámetros
    Defina una lista vacía con capacidad para 10 elementos
    Inicaliza un bucle for que itera por cada elemento de la lista
    Por cada iteración le solicita al usuario que ingrese un nombre
    Ese nombre se guarda dentro de la lista vacía
    Al finalizar el bucle, se imprime en consola un mensaje anunciando los nombres ingresados, y se retorna la lista completa
    """
    ListaNombres = [0] * 10

    for i in range(len(ListaNombres)):
        Nombre = input("Porfavor, ingrese un nombre\n")
        ListaNombres[i] = Nombre
    print("Los nombres ingresados son:")
    return ListaNombres

# Ejercicio 2
def PedirListaNúmeros () -> list:
    """
    No recibe parámetros
    Defina una lista vacía con capacidad para 10 elementos
    Inicaliza un bucle for que itera por cada elemento de la lista
    Por cada iteración le solicita al usuario que ingrese un número y la posición donde desea colocarlo
    Ese número se guarda dentro de la lista vacía, en el índice ingresado
    Al finalizar el bucle, se imprime en consola un mensaje anunciando los números ingresados, y se retorna la lista completa
    """
    ListaNúmeros = [0] * 10
    
    for i in range(len(ListaNúmeros)):
        Número = int(input("Porfavor, ingrese un número\n"))
        Posición = int(input("Porfavor, ingrese la posición en donde desea colocar el número previamente ingresado\n"))
        ListaNúmeros[Posición] = Número
    print("Los números ingresados son:")
    return ListaNúmeros

# Ejercicio 3
def PedirListaNúmerosEnRango () -> list:
    """
    No recibe parámetros
    Defina una lista vacía con capacidad para 10 elementos
    Defina las variables de rango con números aleatorios entre el 1 y el 100
    Inicializa bucles while para asegurar que el rango sea coherente, es decir, hasta no sea menor que desde, y que haya al menos 10 números de diferencia entre cada número, para no tener que ingresar siempre los mismos
    Inicializa un bucle for que itera por cada elemento de la lista
    Por cada iteración le solicita al usuario que ingrese un número dentro del rango generado
    Utiliza un bucle while para validar que el número se encuentre dentro del rango; de no ser así seguirá pidiendo un número que sea válido
    Guarda el número validado dentro de la lista
    Al finalizar el bucle, se imprime en consola un mensaje anunciando los números ingresados, y se retorna la lista completa
    """
    ListaNúmerosEnRango = [0] * 10
    Desde = random.randint(1, 100)
    Hasta = random.randint(1, 100)

    while Hasta <= Desde:
        Hasta = random.randint(1, 100)
    while Desde + 10 >= Hasta:
        Hasta = random.randint(1, 100)

    for i in range(len(ListaNúmerosEnRango)):
        Número = int(input(f"Porfavor, ingrese un número dentro del rango disponible ({Desde} - {Hasta})\n"))
        while not (Desde <= Número <= Hasta):
            Número = int(input(f"El número ingresado no se encuentra del rango disponible. Porfavor, vuelva a ingresar un número dentro del rango disponible ({Desde} - {Hasta})\n"))
        ListaNúmerosEnRango[i] = Número
    print("Los números ingresados son:")
    return ListaNúmerosEnRango

# Ejercicio 4
def EncontrarNúmeroEnLista (lista: list, número: int) -> bool:
    """
    Recibe como parámetros una lista y un número
    Imprime por consola el número que se debe buscar dentro de la lista recibida
    Inicializa un bucle for que itera por cada elemento de la lista
    Por cada iteración, imprime el elemento y verifica si es el número que se está buscando
    De ser correcto, devuelve True; sino, continúa la búsqueda
    Si el bucle finaliza y no se encontró el número pedido, devuelve False
    """
    print(f"El número a encontrar es {número}. Comenzando búsqueda...")
    for i in range(len(lista)):
        print(lista[i])
        if lista[i] == número:
            return True
    return False

# Ejercicio 5
def EncontrarPersonaMenor(lista: list) -> list:
    """
    Recibe una lista como parámetro
    Define una lista de nombres, una variable para almacenar la edad mínima encontrada y una lista vacía de las personas con menor edad
    Inicializa un bucle for que itera por cada elemento de la lista recibida como parámetro
    Por cada iteración, verifica si el elemennto es igual o menor que el último número mínimo registrado
    De ser así, el elemento pasa a ser el nuevo número mínimo, y se suma a la lista de personas con menor edad el nombre de la persona que corresponda con la edad de la lista recibida como parámetro
    Finalmente, devuelve la lista con todas las personas que tienen la edad mínima
    """
    Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofía","María","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
    EdadMenor = float("inf")
    PersonasMenores = []

    for i in range(len(lista)):
        if lista[i] <= EdadMenor:
            EdadMenor = lista[i]
            PersonasMenores.append(Nombres[i])
    return PersonasMenores

# Ejercicio 6
def MostrarNombres(lista: list):
    """
    Recibe una lista como parámetro
    Incializa un bucle for que itera por cada elemento de la lista recibida
    Imprime el elemento guardado en cada iteración
    """
    for i in range(len(lista)):
        print(lista[i])

# Ejercicio 7 y 8
def MostrarMenúOpciones():
    ListasImportadas = False
    Listas = []
    
    def ImportarListas() -> list:
        """
        No recibe ningún parámetro
        Importa todas las listas de listas_personas.py y las devuelve
        """
        from listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades
        return nombres, telefonos, mails, address, postalZip, region, country, edades

    def ListarDatosMéxico(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios de México
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el país es "Mexico"
        De ser así, imprime los datos del usuario
        """
        print("\nLos datos de los usuarios de México son los siguientes:")
        for i in range(len(country)):
            if country[i] == "Mexico":
                print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}\nDirreciones: {address[i]}\nCódigo postal: {postalZip[i]}\nRegión: {region[i]}\nEdad: {edades[i]}")

    def ListarDatosBrasil(nombres, telefonos, mails, country):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios de Brasil
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el país es "Brazil"
        De ser así, imprime los datos del usuario
        """
        print("\nLos datos de los usuarios de Brasil son los siguientes:")
        for i in range(len(country)):
            if country[i] == "Brazil":
                print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}")
    
    def ListarDatosJóvenes(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Declara una variable para guardar la edad mínima encontrada
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios más jóvenes
        Inicializa un bucle for que itera por cada elemento de edades
        Verifica si el elemento de edades es igual o menor que la última edad mínima registrada
        De ser así, el elemento se convierte en la nueva edad mínima y se imprimen los demás datos de las otras listas 
        """
        EdadMínima = float("inf")

        print("\nLos datos de los usuarios más jóvenes son los siguientes:")
        for i in range(len(edades)):
            if edades[i] <= EdadMínima:
                EdadMínima = edades[i]
                print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}\nDirreciones: {address[i]}\nCódigo postal: {postalZip[i]}\nRegión: {region[i]}\nPaís: {country[i]}\nEdad: {edades[i]}")

    def PromediarEdades(edades):
        """
        Recibe como parámetro una lista que contiene edades de los usuarios
        Declara un contador y acumulador vacíos para poder usarlos más tardes para calcular el promedio
        Inicializa un bucle for que itera por cada elemento de edades
        En cada iteración suma 1 al contador y suma el elemento de edades al acumulador
        Al finalizar el bucle, calcula el promedio y lo imprime
        """
        Contador = 0
        Acumulador = 0

        for i in range(len(edades)):
            Contador += 1
            Acumulador += edades[i]
        Promedio = Acumulador / Contador
        print(f"\nEl promedio de edad de los usuarios es de {Promedio} años\n")

    def ListarDatosMayorBrasil(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Declara una variable para guardar la edad máxima encontrada
        Imprime un mensaje introductorio antes de mostrar los datos del usuarios brasileño más anciano
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el elemento de country es "Brazil"
        De ser así, verifica si el elemento es mayor o igual que la última edad máxima registrada
        De ser así, el elemento se convierte en la nueva edad máxima y se imprimen los demás datos de las otras listas 
        """
        EdadMáxima = float("-inf")

        print("\nLos datos del usuario más anciano de Brasil son los siguientes:")
        for i in range(len(country)):
            if country[i] == "Brazil":
                if edades[i] >= EdadMáxima:
                    EdadMáxima = edades[i]
                    print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}\nDirreciones: {address[i]}\nCódigo postal: {postalZip[i]}\nRegión: {region[i]}\nEdad: {edades[i]}")

    def ListarDatosPostalesMéxicoBrasil(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios de México y Brasil cuyo código postal es mayor a 8000
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el país es "Mexico" o "Brazil"
        De ser así, verifica si el código postal es mayor o igual a 8000
        De ser así, imprime los datos del usuario
        """
        print("\nLos datos de los usuarios de México y Brasil con un código postal mayor a 8000 son los siguientes:")
        for i in range(len(country)):
            if country[i] == "Mexico" or country[i] == "Brazil":
                if postalZip[i] >= 8000:
                    print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}\nDirreciones: {address[i]}\nCódigo postal: {postalZip[i]}\nRegión: {region[i]}\nPaís: {country[i]}\nEdad: {edades[i]}")

    def ListarDatosAdultosItalia(nombres, telefonos, mails, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios de Italia mayores a 40 años
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el país es "Italy"
        De ser así, verifica si la edad es igual o mayor a 40
        De ser así, imprime los datos del usuario
        """
        print("\nLos datos de los usuarios de Italia mayores a 40 años son los siguientes:")
        for i in range(len(country)):
            if country[i] == "Italy":
                if edades[i] >= 40:
                    print(f"\nNombre: {nombres[i]}\nTeléfono: {telefonos[i]}\nCorreo electrónico: {mails[i]}\nEdad: {edades[i]}")
    
    while True:
        OpciónElegida = int(input("Bienvenido a la base de datos del sitio. Elija la opción que le gustaría realizar\n1) Importar Listas\n2) Listar los datos de los usuarios de México\n3) Listar los nombre, mail y teléfono de los usuarios de Brasil\n4) Listar los datos de los usuarios más jovenes\n5) Obtener un promedio de edad de los usuarios\n6) Listar los datos del usuario de mayor edad de Brasil\n7) Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8) Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n"))

        if OpciónElegida == 1:
            Listas = ImportarListas()
            print("\nLas listas fueron importadas con éxito\n")
            ListasImportadas = True
        elif OpciónElegida == 2 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosMéxico(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 3 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosBrasil(nombres, telefonos, mails, country)
        elif OpciónElegida == 4 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosJóvenes(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 5 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            PromediarEdades(edades)
        elif OpciónElegida == 6 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosMayorBrasil(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 7 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosPostalesMéxicoBrasil(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 8 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosAdultosItalia(nombres, telefonos, mails, country, edades)
        else:
            print("Las listas no han sido importadas, por lo que no se pueden realizar las demás operaciones. Importe las listas si desea realizar otras acciones")
            break