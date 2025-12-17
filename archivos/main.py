from Funciones import *
# Ejercicio 1) Crear la función leer_json() que va a recibir el nombre y extensión de donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el nombre de la lista a leer por ejemplo en la imagen anterior la lista está en la clave "heroes" Si el archivo existe deberia leer el archivo json y retornar la lista obtenida. Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)
try:
    contenido_json = leer_json("data_stark.json", "heroes")
    for línea in contenido_json:
        print(json.dumps(línea, ensure_ascii=False, indent=4))
except FileNotFoundError:
    print("\nNo se ha encontrado un archivo con el nombre ingresado.")
except KeyError:
    print("\nNo se ha encontrado ninguna lista con la clave ingresada.")
# Ejercicio 2 y 3) Crear la función generar_csv(). La función va a recibir el nombre y extensión del archivo csv de los superhéroes (Puede ser ruta absoluta o relativa) y la lista de los mismos. Si la lista no está vacía la función deberá guardar en un string la información en formato csv (separado con comas) con la cabecera correspondiente. Una vez generado el string debería usar la función del siguiente punto para guardar ese string generado al archivo. Si la lista está vacía, retornar False. 
# Crear la función "guardar_archivo" la cual recibirá por parámetro un string que indicará el nombre con el cual se guardará el archivo junto con su extensión (ejemplo: "archivo.csv") y como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo. Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso de existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario False (VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá imprimir un mensaje respetando el formato: Se creó el archivo: nombre_archivo.csv. ATENCIÓN: Controlar las excepciones posibles en caso de presentarse alguna retornar false e imprimir un mensaje que diga: "Error al crear el archivo: nombre_archivo" Donde nombre_archivo será el nombre que recibirá el archivo a ser creado, conjuntamente con su extensión.
try:
    contenido_csv = generar_csv("data_stark.json", "heroes", "héroes.csv")
except FileNotFoundError:
    print("\nNo se ha encontrado un archivo con el nombre ingresado.")
except KeyError:
    print("\nNo se ha encontrado ninguna lista con la clave ingresada.")
# Ejercicio 4) Crear un menú con las siguientes opciones: 1) Leer archivo JSON, 2) Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente, 3) Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario, 4) Salir. Crear una función para cada opción de menú.
mostrar_menú_de_opciones()