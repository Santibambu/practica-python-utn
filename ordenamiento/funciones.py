# Ejercicio 1) Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente
def OrdenarNombres(nombres:list) -> list:
    """
    Recibe una lista como parámetro, para poder odenarla
    Inicaliza un bucle for que itera por cada elemento de la lista
    Inicaliza otro bucle for que itera por cada iteración del primer bucle
    Compara si la primera iteración es mayor a la segunda
    De ser así, se crea una variable auxiliar para almacenar temporalmente el valor de la primera iteración
    Luego, la primera iteración toma el valor de la segunda, y la segunda toma el valor de la variable auxiliar, completando el intercambio
    Al finalizar el bucle, se devuelve la lista ya ordenada
    """
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if(nombres[i] > nombres[j]):
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
    return nombres

# Ejercicio 2) Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente
def OrdenarMaterias(nombres: list, puntos: list) -> list:
    """
    Recibe dos listas como parámetros: una de nombres para poder ordenarla de manera ascendente, y otra de puntos, en caso de que los nombres sean iguales
    Inicializa un bucle for que itera por todos los elementos de la lista de nombres
    Inicializa otro bucle for que itera por cada iteración del primer bucle
    Verifica si el nombre del primer bucle es mayor al segundo
    De ser así, se crea una variable auxiliar para almacenar temporalmente el valor de la primera iteración
    Luego, la primera iteración toma el valor de la segunda, y la segunda toma el valor de la variable auxiliar, completando el intercambio
    En cambio, si el nombre del primer bucle es igual al del segundo bucle, verifica si la cantidad de puntos del primer bucle es menor a la cantidad de puntos del segundo bucle
    De ser así, nuevamente se crea una variable auxiliar para almacenar temporalmente el valor de la primera iteración
    Luego, la primera iteración toma el valor de la segunda, y la segunda toma el valor de la variable auxiliar, completando el intercambio
    Al finalizar el bucle, se devuelve la lista ya ordenada
    """
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if(nombres[i] > nombres[j]):
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
            elif(nombres[i] == nombres[j]):
                if(puntos[i] < puntos[j]):
                    aux = puntos[i]
                    puntos[i] = puntos[j]
                    puntos[j] = aux
    return nombres

# Ejercicio 3) Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente
def OrdenarEstudiantes(estudiantes: list, apellidos: list, notas:list) -> list:
    """
    
    """
    for i in range(len(apellidos) - 1):
        for j in range(i + 1, len(apellidos)):
            if(apellidos[i] > apellidos[j]):
                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux
            elif(apellidos[i] == apellidos[j]):
                if(estudiantes[i] > estudiantes[j]):
                    aux = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = aux
            elif(estudiantes[i] == estudiantes[j]):
                if(notas[i] < notas[j]):
                    aux = notas[i]
                    notas[i] = notas[j]
                    notas[j] = aux
    return apellidos, estudiantes, notas

# Ejericio 4)
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

    def ListarDatosNombresMexicanos(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios de México
        Inicaliza una variable para guardar los datos de los usuarios de México dentro de una lista
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el país es "Mexico"
        De ser así, guarda los datos en la lista de México
        Inicaliza otro bucle for que itera por cada dato de las personas de México, y otro más que itera por cada iteración del primer bucle
        Allí se verifica que los datos estén ordenados de manera alfabetica y se realiza un intercambio de valores de ser necesario
        Finalmente, se imprimen los datos dentro de una "tabla" con marcadores y separadores
        """
        print("\nLos datos de los usuarios de México, ordenados alfabeticamente por nombre, son los siguientes:\n")
        
        DatosMexicanos = []
        for i in range(len(country)):
            if country[i] == "Mexico":
                DatosMexicanos.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], edades[i]])

        for i in range(len(DatosMexicanos) - 1):
            for j in range(len(DatosMexicanos) - i - 1):
                if DatosMexicanos[j][0] > DatosMexicanos[j + 1][0]:
                    DatosMexicanos[j], DatosMexicanos[j + 1] = DatosMexicanos[j + 1], DatosMexicanos[j]

        print(f"{'Nombre':<17} {'Teléfono':<15} {'Email':<20} {'Dirección':<25} {'C.P.':<10} {'Región':<15} {'Edad':<5}")
        print("-" * 111)
        for fila in DatosMexicanos:
            print(f"{fila[0]:<17} {fila[1]:<15} {fila[2]:<20} {fila[3]:<25} {fila[4]:<10} {fila[5]:<15} {fila[6]:<5}")

    def ListarDatosJóvenesEdad(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios más jóvenes
        Declara una lista vacía para guardar los datos de los usuarios más jóvenes y una variable para guardar la edad mínima encontrada
        Inicializa un bucle for que itera por cada elemento de edades
        Verifica si el elemento de edades es igual o menor que la última edad mínima registrada
        De ser así, el elemento se convierte en la nueva edad mínima y se guardan los datos en la lista de usuarios jóvenes
        Inicaliza otro bucle for que itera por cada dato de las personas de México, y otro más que itera por cada iteración del primer bucle
        Allí se verifica que los datos estén ordenados de manera alfabetica y se realiza un intercambio de valores de ser necesario
        Finalmente, se imprimen los datos dentro de una "tabla" con marcadores y separadores
        """
        print("\nLos datos de los usuarios más jóvenes, ordenados alfabeticamente por nombre, son los siguientes:\n")

        DatosJóvenes = []
        EdadMínima = float("inf")
        for i in range(len(edades)):
            if edades[i] <= EdadMínima:
                EdadMínima = edades[i]
                DatosJóvenes.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]])

        for i in range(len(DatosJóvenes) - 1):
            for j in range(len(DatosJóvenes) - i - 1):
                if DatosJóvenes[j][0] > DatosJóvenes[j + 1][0]:
                    DatosJóvenes[j], DatosJóvenes[j + 1] = DatosJóvenes[j + 1], DatosJóvenes[j]

        print(f"{'Nombre':<18} {'Teléfono':<17} {'Email':<30} {'Dirección':<30}")
        print("-" * 95)
        for fila in DatosJóvenes:
            print(f"{fila[0]:<18} {fila[1]:<17} {fila[2]:<30} {fila[3]:<30}")

        print("\n")

        print(f"{'C.P.':<12} {'Región':<18} {'País':<18} {'Edad':<7}")
        print("-" * 55)
        for fila in DatosJóvenes:
            print(f"{fila[4]:<12} {fila[5]:<18} {fila[6]:<18} {fila[7]:<7}")

    def ListarDatosPostalesMéxicoBrasilOrdenados(nombres, telefonos, mails, address, postalZip, region, country, edades):
        """
        Recibe como parámetros las listas importadas que contienen datos de usuarios
        Imprime un mensaje introductorio antes de mostrar los datos de los usuarios más jóvenes
        Declara una lista vacía para guardar los datos de los usuarios de México y Brasil con un código postal mayor a 8000
        Inicializa un bucle for que itera por cada elemento de country
        Verifica si el elemento de country es igual a "Mexico" o "Brazil", y luego verifica si el código postal es mayor a 8000
        De ser así, se guardan los datos en la lista de datos postales
        Inicaliza otro bucle for que itera por cada dato de las personas con los datos postales, y otro más que itera por cada iteración del primer bucle
        Allí se verifica que los datos estén ordenados de manera alfabetica (y por edades, si el nombre es el mismo) y se realiza un intercambio de valores de ser necesario
        Finalmente, se imprimen los datos dentro de una "tabla" con marcadores y separadores
        """
        print("\nLos datos de los usuarios de México y Brasil con un código postal mayor a 8000, ordenados por nombre y edad, son los siguientes:")

        DatosPostales = []
        for i in range(len(country)):
            if country[i] == "Mexico" or country[i] == "Brazil":
                if postalZip[i] >= 8000:
                    DatosPostales.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]])

        for i in range(len(DatosPostales) - 1):
            for j in range(len(DatosPostales) - i - 1):
                if DatosPostales[j][0] > DatosPostales[j + 1][0]:
                    DatosPostales[j], DatosPostales[j + 1] = DatosPostales[j + 1], DatosPostales[j]
                elif DatosPostales[j][7] > DatosPostales[j + 1][7]:
                    DatosPostales[j], DatosPostales[j + 1] = DatosPostales[j + 1], DatosPostales[j]

        print(f"{'Nombre':<18} {'Teléfono':<17} {'Email':<30} {'Dirección':<30}")
        print("-" * 95)
        for fila in DatosPostales:
            print(f"{fila[0]:<18} {fila[1]:<17} {fila[2]:<30} {fila[3]:<30}")

        print("\n")

        print(f"{'C.P.':<12} {'Región':<18} {'País':<18} {'Edad':<7}")
        print("-" * 55)
        for fila in DatosPostales:
            print(f"{fila[4]:<12} {fila[5]:<18} {fila[6]:<18} {fila[7]:<7}")
        
    while True:
        OpciónElegida = int(input("\nBienvenido a la base de datos del sitio. Elija la opción que le gustaría realizar\n1) Importar Listas\n2) Listar los datos de los usuarios de México\n3) Listar los nombre, mail y teléfono de los usuarios de Brasil\n4) Listar los datos de los usuarios más jovenes\n5) Obtener un promedio de edad de los usuarios\n6) Listar los datos del usuario de mayor edad de Brasil\n7) Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8) Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n9) Listar los datos de los usuarios de México ordenados por nombre\n10) Listar los datos de los usuarios más jóvenes ordenados por edad de manera ascendente (Si la edad se repite, se ordenan por nombre de manera ascendente)\n11) Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente\n"))

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
        elif OpciónElegida == 9 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosNombresMexicanos(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 10 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosJóvenesEdad(nombres, telefonos, mails, address, postalZip, region, country, edades)
        elif OpciónElegida == 11 and ListasImportadas == True:
            nombres, telefonos, mails, address, postalZip, region, country, edades = Listas
            ListarDatosPostalesMéxicoBrasilOrdenados(nombres, telefonos, mails, address, postalZip, region, country, edades)
        else:
            print("Las listas no han sido importadas, por lo que no se pueden realizar las demás operaciones. Importe las listas si desea realizar otras acciones")
            break