import json
# Ejercicio 1) Crear la función leer_json() que va a recibir el nombre y extensión de donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el nombre de la lista a leer por ejemplo en la imagen anterior la lista está en la clave "heroes" Si el archivo existe deberia leer el archivo json y retornar la lista obtenida. Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)
def leer_json(nombre_archivo: str, clave:str) -> list | bool:
    with open(nombre_archivo, "r") as archivo:
        if archivo:
            texto = json.load(archivo)
            resultado = texto[clave]
        else:
            resultado = False
    return resultado
# Ejercicio 2) Crear la función generar_csv(). La función va a recibir el nombre y extensión del archivo csv de los superhéroes (Puede ser ruta absoluta o relativa) y la lista de los mismos. Si la lista no está vacía la función deberá guardar en un string la información en formato csv (separado con comas) con la cabecera correspondiente. Una vez generado el string debería usar la función del siguiente punto para guardar ese string generado al archivo. Si la lista está vacía, retornar False.
def generar_csv(nombre_json:str, clave:str, nombre_csv:str) -> bool:
    lista = leer_json(nombre_json, clave)

    if not lista:
        print("La lista ingresada está vacía.")
        resultado = False
    else:
        contenido_csv = convertir_lista_a_csv(lista)
        resultado = guardar_archivo(nombre_csv, contenido_csv)
    return resultado

def convertir_lista_a_csv(lista:list) -> str:
    csv = "nombre,identidad,altura,peso,fuerza,inteligencia\n"
    for héroe in lista:
        fila = f"{héroe["nombre"]},{héroe["identidad"]},{héroe["altura"]},{héroe["peso"]},{héroe["fuerza"]},{héroe["inteligencia"]}\n"
        csv += fila
    return csv
# Ejercicio 3) Crear la función "guardar_archivo" la cual recibirá por parámetro un string que indicará el nombre con el cual se guardará el archivo junto con su extensión (ejemplo: "archivo.csv") y como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo. Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso de existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario False (VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá imprimir un mensaje respetando el formato: Se creó el archivo: nombre_archivo.csv. ATENCIÓN: Controlar las excepciones posibles en caso de presentarse alguna retornar false e imprimir un mensaje que diga: "Error al crear el archivo: nombre_archivo" Donde nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su extensión.
def guardar_archivo (nombre_archivo:str, contenido:str) -> bool:
    try:
        with open (nombre_archivo, "w+") as archivo:
            archivo.write(contenido)
            print(f"\nSe creó el archivo: {nombre_archivo}")
            resultado = True
    except Exception:
        print(f"\nError al crear el archivo:{nombre_archivo}")
        resultado = False
    return resultado
# Ejercicio 4) Crear un menú con las siguientes opciones: 1) Leer archivo JSON, 2) Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente, 3) Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario, 4) Salir. Crear una función para cada opción de menú.

def mostrar_menú_de_opciones():
    """
    Muestra un menú de opciones al usuario y ejecuta acciones según la opción elegida.
    Parámetros:
        Ninguno.
    """
    while True:
        try:
            opción_elegida = int(input("\nBienvenido. Elija la opción que le gustaría realizar:\n1) Leer archivo JSON\n2) Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente y guardar el listado ordenado en un CSV (opcional)\n3) Salir\n"))

            if opción_elegida == 1:
                try:
                    contenido_json = leer_json("data_stark.json", "heroes")
                    for línea in contenido_json:
                        print(json.dumps(línea, ensure_ascii=False, indent=4))
                except FileNotFoundError:
                    print("\nNo se ha encontrado un archivo con el nombre ingresado.")
                except KeyError:
                    print("\nNo se ha encontrado ninguna lista con la clave ingresada.")
            elif opción_elegida == 2:
                try:
                    ordenamiento = int(input("\nSeleccione la clave por la cual desea ordenar a los héroes:\n1) Altura\n2) Peso\n3) Fuerza\n"))
                    if ordenamiento == 1:
                        héroes_ordenados_altura = procesar_héroes(("data_stark.json", "heroes"), tipos_ordenamiento["altura"])
                        print(f"\nLista de héroes ordenados por altura de menor a mayor:")
                        for héroes in héroes_ordenados_altura:
                            print(f"- {héroes["nombre"]} ({héroes["altura"]})")

                        guardar_lista = input("\n¿Desea guardar la lista creada en un archivo CSV? (S/N)\n").upper()
                        if guardar_lista in ["S"]:
                            nombre_archivo = input("\nIngrese el nombre del archivo que desea crear:\n")
                            csv_altura = convertir_lista_a_csv(héroes_ordenados_altura)
                            guardar_archivo(nombre_archivo, csv_altura)
                    elif ordenamiento == 2:
                        héroes_ordenados_peso = procesar_héroes(("data_stark.json", "heroes"), tipos_ordenamiento["peso"])
                        print(f"\nLista de héroes ordenados por peso de menor a mayor:")
                        for héroes in héroes_ordenados_peso:
                            print(f"- {héroes["nombre"]} ({héroes["peso"]})")

                        guardar_lista = input("\n¿Desea guardar la lista creada en un archivo CSV? (S/N)\n").upper()
                        if guardar_lista in ["S"]:
                            nombre_archivo = input("\nIngrese el nombre del archivo que desea crear:\n")
                            csv_peso = convertir_lista_a_csv(héroes_ordenados_peso)
                            guardar_archivo(nombre_archivo, csv_peso)
                    elif ordenamiento == 3:
                        héroes_ordenados_fuerza = procesar_héroes(("data_stark.json", "heroes"), tipos_ordenamiento["fuerza"])
                        print(f"\nLista de héroes ordenados por fuerza de menor a mayor:")
                        for héroes in héroes_ordenados_fuerza:
                            print(f"- {héroes["nombre"]} ({héroes["fuerza"]})")

                        guardar_lista = input("\n¿Desea guardar la lista creada en un archivo CSV? (S/N)\n").upper()
                        if guardar_lista in ["S"]:
                            nombre_archivo = input("\nIngrese el nombre del archivo que desea crear:\n")
                            csv_fuerza = convertir_lista_a_csv(héroes_ordenados_fuerza)
                            guardar_archivo(nombre_archivo, csv_fuerza)
                    else:
                        raise ValueError
                except ValueError:
                    print("\nLa opción ingresada no es válida. Vuelva a intentarlo.")     
            elif opción_elegida == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nLa opción ingresada no es válida. Vuelva a intentarlo.")

def procesar_héroes(parámetros:tuple, función:callable) -> list:
    nombre_archivo, clave = parámetros
    return función(nombre_archivo, clave)

def extraer_valor_diccionario(clave:str) -> str | int:
    def extraer_valor(valor: dict):
        return valor[clave]
    return extraer_valor

def ordenar_json_criterio(criterio:str) -> list:
    def ordenar_json(nombre_archivo:str, clave:str):
        json = leer_json(nombre_archivo, clave)
        clave_ordenamiento = extraer_valor_diccionario(criterio)
        json.sort(key=clave_ordenamiento)
        return json
    return ordenar_json

tipos_ordenamiento = {
    "altura": ordenar_json_criterio("altura"),
    "peso": ordenar_json_criterio("peso"),
    "fuerza": ordenar_json_criterio("fuerza")
}