# Ejercicio 1) El almacén de barrio precisa un programa para almacenar, ordenar y controlar stock de su mercadería por día. Armar la matriz de productos con nombre, cantidad y ubicación (fila, columna)
Góndola = [[[], ["Botellas", 3], [], ["Frascos", 8], []],
           [[], [], ["Fideos", 4], [], []],
           [[], [], [], ["Leche", 6], []]]

# Ejercicios 2 y 3) Armar un menú de opciones
def MostrarMenú():

    def AgregarProducto(matriz: list):
        """
        Solicita al usuario los datos necesarios para agregar un producto a la góndola.
        Permite seleccionar la ubicación (fila y columna) donde se agregará el producto,
        Valida que la celda esté vacía y que los datos ingresados sean correctos.
        Si la operación es exitosa, agrega el producto y su cantidad en la celda indicada.
        En caso de error en los datos ingresados, muestra un mensaje y vuelve a solicitar los datos.

        Parámetros:
        matriz (list): Matriz que representa la góndola, donde se almacenan los productos.
        """
        while True:
            try:
                Fila = int(input("Ingrese la fila de la góndola en la que desea agregar el producto (desde 0 hasta 2): \n"))
                if Fila < 0 or Fila > 2:
                    raise ValueError("el número de la fila debe de estar dentro del rango 0-2\n")
                Columna = int(input("Ingrese la columna de la góndola en la que desea agregar el producto (desde 0 hasta 4): \n"))
                if Columna < 0 or Columna > 4:
                    raise ValueError("el número de la columna debe de estar dentro del rango 0-4\n")
                if matriz[Fila][Columna] != []:
                    raise ValueError("la celda seleccionada debe de estar vacía\n")
                Cantidad = int(input("Ingrese la cantidad del producto que desea agregar: \n"))
                if Cantidad <= 0:
                    raise ValueError("la cantidad de productos a agregar debe ser mayor a 0\n")
                Producto = input("Ingrese el nombre del producto que desea agregar: \n")
                matriz[Fila][Columna] = [Producto, Cantidad]
                print(f"El producto se ha agregado exitosamente en la celda {Fila}, {Columna}. Los contenidos se verán así: {matriz[Fila][Columna]}\n")
                break
            except ValueError as e:
                print(f"Se ha producido un error: {e}")

    def EliminarProducto(matriz: list):
        """
        Permite eliminar un producto de la góndola solicitando al usuario la ubicación (fila y columna).
        Valida que la celda seleccionada contenga un producto y solicita confirmación antes de eliminarlo.
        Si la operación es exitosa, elimina el producto de la celda indicada.
        En caso de error en los datos ingresados o si la celda está vacía, muestra un mensaje y vuelve a solicitar los datos.

        Parámetros:
        matriz (list): Matriz que representa la góndola, donde se almacenan los productos.
        """
        while True:
            try:
                Fila = int(input("Ingrese la fila de la góndola en la que desea eliminar un producto (desde 0 hasta 2): \n"))
                if Fila < 0 or Fila > 2:
                    raise ValueError("el número de la fila debe de estar dentro del rango 0-2\n")
                Columna = int(input("Ingrese la columna de la góndola en la que desea eliminar un producto (desde 0 hasta 4): \n"))
                if Columna < 0 or Columna > 4:
                    raise ValueError("el número de la columna debe de estar dentro del rango 0-4\n")
                if matriz[Fila][Columna] == []:
                    raise ValueError("la celda seleccionada no debe estar vacía")
                Confirmación = (input(f"Está a punto de eliminar el producto de la celda {Fila}, {Columna}. ¿Está seguro que desea continuar? (S/N)\n")).upper()
                if Confirmación not in ["S", "N"]:
                    raise ValueError("la confirmación debe ser S o N")
                elif Confirmación == "S":
                    matriz[Fila][Columna].clear()
                    print(f"La operación se ha realizado con éxito. La celda ahora está vacía")
                else:
                    print("Ha decidio no eliminar el prdoucto. Volviendo al menú de opciones")
                    break
                break
            except ValueError as e:
                print(f"Se ha producido un error: {e}")

    def ModificarProducto(matriz: list):
        """
        Permite modificar la cantidad de un producto existente en la góndola.
        Solicita al usuario la ubicación (fila y columna), el tipo de operación (agregar o restar) y la cantidad a modificar.
        Valida que la celda contenga un producto y que la operación sea válida.
        Si la cantidad llega a cero tras la resta, elimina el producto de la celda.
        En caso de error en los datos ingresados, muestra un mensaje y vuelve a solicitar los datos.

        Parámetros:
        matriz (list): Matriz que representa la góndola, donde se almacenan los productos.
        """
        while True:
            try:
                Fila = int(input("Ingrese la fila de la góndola en la que desea modificar un producto (desde 0 hasta 2): \n"))
                if Fila < 0 or Fila > 2:
                    raise ValueError("el número de la fila debe de estar dentro del rango 0-2\n")
                Columna = int(input("Ingrese la columna de la góndola en la que desea modificar un producto (desde 0 hasta 4): \n"))
                if Columna < 0 or Columna > 4:
                    raise ValueError("el número de la columna debe de estar dentro del rango 0-4\n")
                if matriz[Fila][Columna] == []:
                    raise ValueError("la celda seleccionada no debe estar vacía\n")
                Operación = input("¿Qué operación le gustaría realizar? ¿Agregar o Resta? (A/R)\n" ).upper()
                if Operación not in ["A", "R"]:
                    raise ValueError("la operación debe ser A o R\n")
                Cantidad = int(input(f"Ingrese la cantidad del producto que desea modificar ({matriz[Fila][Columna][1]} productos existentes) \n"))
                Confirmación = (input(f"Está a punto de modificar los elementos {matriz[Fila][Columna]} de la celda {Fila}, {Columna}. ¿Está seguro que desea continuar? (S/N)\n")).upper()
                if Confirmación not in ["S", "N"]:
                    raise ValueError("la confirmación debe ser S o N\n")
                elif Confirmación == "S":
                    pass
                else:
                    print("Ha decidido no realizar la modificación. Volviendo al menú de opciones\n")
                    break
                if Operación == "A":
                    if Cantidad <= 0:
                        raise ValueError("la cantidad de productos a agregar no puede ser 0 o menos\n")
                    matriz[Fila][Columna][1] += Cantidad
                    print(f"La operación se ha realizado con éxito. La celda aparecerá como: {matriz[Fila][Columna]}")
                elif Cantidad <= 0 or Cantidad > matriz[Fila][Columna][1]:
                    raise ValueError("la cantidad de productos a eliminar no puede sobrepasar la cantidad de productos existentes ni ser 0 o menos\n")
                else:
                    matriz[Fila][Columna][1] -= Cantidad
                    if matriz[Fila][Columna][1] == 0:
                        matriz[Fila][Columna].clear()
                        print(f"La operación se ha realizado con éxito. La celda aparecerá como: {matriz[Fila][Columna]}\n")
                break
            except ValueError as e:
                print(f"Se ha producido un error: {e}")   
    
    def ImprimirGóndola(matriz: list):
        """
        Muestra los productos de la góndola en forma de tabla.
        Las celdas vacías se muestran como "-" y las ocupadas muestran el nombre y cantidad del producto.
        """
        matriz_str = []
        for fila in matriz:
            fila_str = []
            for celda in fila:
                if celda == []:
                    fila_str.append("-")
                else:
                    fila_str.append(f"{celda[0]} ({celda[1]})")
            matriz_str.append(fila_str)
        anchos = [max(len(celda) for celda in columna) for columna in zip(*matriz_str)]
        print("\nLos contenidos de la góndola son los siguientes:\n")
        for fila in matriz_str:
            fila_impresa = "|".join(f" {celda.center(anchos[i])} " for i, celda in enumerate(fila))
            print(f"|{fila_impresa}|")

    def ListarProductos(matriz: list):
        """
        Toma la góndola (matriz), extrae todos los productos y los imprime ordenados alfabéticamente por nombre usando bubble sort.
        Las celdas vacías se ignoran.
        """
        Productos = []
        for fila in matriz:
            for celda in fila:
                if celda != []:
                    Productos.append((celda[0], celda[1]))
        for i in range(len(Productos)):
            for j in range(len(Productos) - 1):
                if Productos[j][0] > Productos[j + 1][0]:
                    Productos[j], Productos[j + 1] = Productos[j + 1], Productos[j]
        print("\nLa lista de productos de la góndola ordenados alfabéticamente es la siguiente:")
        for nombre, cantidad in Productos:
            print(f"- {nombre} ({cantidad})")

    while True:
        OpciónElegida = int(input("\nBienvenido a la base de datos del almacén. Elija la opción que le gustaría realizar\n1) Agregar un nuevo producto\n2) Eliminar un producto existente\n3) Modificar un producto\n4) Imprimir góndola\n5) Listar productos, ordenados por nombre\n6) Salir\n"))
        if OpciónElegida == 1:
            AgregarProducto(Góndola)
        elif OpciónElegida == 2:
            EliminarProducto(Góndola)
        elif OpciónElegida == 3:
            ModificarProducto(Góndola)
        elif OpciónElegida == 4:
            ImprimirGóndola(Góndola)
        elif OpciónElegida == 5:
            ListarProductos(Góndola)
        elif OpciónElegida == 6:
            print("\nCerrando sesión")
            break
        else:
            print("Se ha seleccionado una opción inválida. Porfavor, vuelva a ingresar la opción que desea realizar\n")

# Ejercicio 5) Desarrollar un programa para el control de stock de una ferretería para sus artículos de tornillos y tarugos. Los mismos se encuentran almacenados en una cajonera de ferretería metálica con cajones. Armar la lista estantería para contener los cajones con listas anidadas
Estantería = [[["Tornillo 12mm", 65], ["Tornillo 16mm", 86], ["Tornillo 20mm", 65], ["Tornillo 25mm", 45]],
             [["Tornillo 30mm", 68], ["Tornillo 35mm", 73], ["Tornillo 40mm", 85], ["Tornillo 45mm", 89]],
             [["Tarugo 4mm", 58], ["Tarugo 5mm", 48], ["Tarugo 6mm", 64], ["Tarugo 7mm", 96]],
             [["Tarugo 8mm", 36], ["Tarugo 10mm", 72], ["Tarugo 12mm", 78], ["Tarugo 14mm", 71]]]

# Ejercicios 6 y 7) Armar un menú de opciones
def MostrarMenúFerretería():

    def ReponerMercadería(matriz:list):
        """
        Permite reponer mercadería en la estantería solicitando al usuario la ubicación (fila y columna) y la cantidad a reponer.
        Valida que la cantidad sea mayor a 0 y que el stock total no supere las 100 unidades.
        Si la operación es exitosa, suma la cantidad indicada al producto correspondiente.
        En caso de error en los datos ingresados, muestra un mensaje y vuelve a solicitar los datos.

        Parámetros:
        matriz (list): Matriz que representa la estantería, donde se almacenan los productos.
        """

        while True:
            try:
                Fila = int(input("Ingrese la fila de la estantería en la que desea reponer la mercadería (desde 0 hasta 3): \n"))
                if Fila < 0 or Fila > 3:
                    raise ValueError("el número de la fila debe de estar dentro del rango 0-3\n")
                Columna = int(input("Ingrese la columna de la estantería en la que desea reponer la mercadería (desde 0 hasta 3): \n"))
                if Columna < 0 or Columna > 3:
                    raise ValueError("el número de la columna debe de estar dentro del rango 0-3\n")
                Cantidad = int(input(f"Ingrese la cantidad de la mercadería que desea reponer (Producto: {matriz[Fila][Columna][0]}, Cantidad: {matriz[Fila][Columna][1]}) \n"))
                if Cantidad <= 0:
                    raise ValueError("la cantidad de mercadería para reponer debe ser mayor a 0\n")
                elif matriz[Fila][Columna][1] + Cantidad > 100:
                    raise ValueError("la cantidad de stock total no puede superar las 100 unidades\n ")
                matriz[Fila][Columna][1] += Cantidad
                print(f"La mercadería se ha repuesto exitosamente en la celda {Fila}, {Columna}. Los contenidos se verán así: {matriz[Fila][Columna]}")
                break
            except ValueError as e:
                print(f"\nSe ha producido un error: {e}")
        
    def VenderMercadería(matriz:list):
        """
        Permite vender mercadería de la estantería solicitando al usuario la ubicación (fila y columna) y la cantidad a vender.
        Valida que la cantidad sea mayor a 0 y que no se venda más de lo disponible en stock.
        Si la operación es exitosa, descuenta la cantidad indicada al producto correspondiente.
        En caso de error en los datos ingresados, muestra un mensaje y vuelve a solicitar los datos.

        Parámetros:
        matriz (list): Matriz que representa la estantería, donde se almacenan los productos.
        """
        while True:
            try:
                Fila = int(input("Ingrese la fila de la estantería en la que desea vender mercadería (desde 0 hasta 3): \n"))
                if Fila < 0 or Fila > 3:
                    raise ValueError("el número de la fila debe de estar dentro del rango 0-3\n")
                Columna = int(input("Ingrese la columna de la estantería en la que desea vender mercadería (desde 0 hasta 3): \n"))
                if Columna < 0 or Columna > 3:
                    raise ValueError("el número de la columna debe de estar dentro del rango 0-3\n")
                Cantidad = int(input(f"Ingrese la cantidad de mercadería que desea vender (Producto: {matriz[Fila][Columna][0]}, Cantidad: {matriz[Fila][Columna][1]}) \n"))
                if Cantidad <= 0:
                    raise ValueError("la cantidad de mercadería para vender debe ser mayor a 0\n")
                elif matriz[Fila][Columna][1] - Cantidad < 0:
                    raise ValueError("el objetivo de venta no puede superar a la cantidad de mercadería disponible\n ")
                matriz[Fila][Columna][1] -= Cantidad
                print(f"La mercadería se ha vendido exitosamente en la celda {Fila}, {Columna}. Los contenidos se verán así: {matriz[Fila][Columna]}")
                break
            except ValueError as e:
                print(f"\nSe ha producido un error: {e}")

    def ImprimirInventario(matriz:list):
        # Muestra los productos de la estantería en forma de tabla.
        matriz_str = []
        for fila in matriz:
            fila_str = []
            for celda in fila:
                if celda == []:
                    fila_str.append("-")
                else:
                    fila_str.append(f"{celda[0]} ({celda[1]})")
            matriz_str.append(fila_str)
        anchos = [max(len(celda) for celda in columna) for columna in zip(*matriz_str)]
        print("\nLos contenidos de la estantería son los siguientes:\n")
        for fila in matriz_str:
            fila_impresa = "|".join(f" {celda.center(anchos[i])} " for i, celda in enumerate(fila))
            print(f"|{fila_impresa}|")

    while True:
        OpciónElegida = int(input("\nBienvenido a la base de datos de la ferretería. Elija la opción que le gustaría realizar\n1) Reponer mercadería\n2) Vender mercadería\n3) Listar inventario\n4) Salir\n"))
        if OpciónElegida == 1:
            ReponerMercadería(Estantería)
        elif OpciónElegida == 2:
            VenderMercadería(Estantería)
        elif OpciónElegida == 3:
            ImprimirInventario(Estantería)
        elif OpciónElegida == 4:
            print("\nCerrando sesión")
            break
        else:
            print("Se ha seleccionado una opción inválida. Porfavor, vuelva a ingresar la opción que desea realizar\n")