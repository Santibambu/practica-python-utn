from Funciones import *
# Ejercicio 1) Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad. Ejemplo: cadena = "murcielaguito"
matriz_vocales = crear_matriz_vocales("Euforia")

print("\nAquí está la tabla con la cantidad de vocales encontradas en la cadena ingresada:\n")
print("-" * 11)
for lista in matriz_vocales:
    vocal = lista[0]
    cantidad = lista[1]
    print(f"| {vocal:^2} | {cantidad:^2} |")
print("-" * 11)

# Ejercicio 2) Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
caracter = encontrar_caracter("Salado", "O")
print(f"\nEl caracter se ha encontrado por primera vez en el índice {caracter}\n")

# Ejercicio 3) Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido
print(es_palíndromo("Neuquen"))

# Ejercicio 4) Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos. Ejemplo: Si recibe como parámetro la cadena "Hooola" debe devolver "Hola".
print(suprimir_caracteres_repetidos("Hoooola, cómo estás? Quería decirte queeeee deberías venir a casssssa para comer un poco del purééé que hace mi papá!!!!"))

# Ejercicio 5) Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma. Ejemplo: Si recibe como parámetro la cadena "Hola" debe devolver "Hl"
print(suprimir_vocales("Aceituna, Estoico, Islandia, Oruga, Universo"))

# Ejercicio 6) Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena. Ejemplo: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
print(contar_subcadenas("Tres tristes tigres comen trigo en un trigal", "tri"))