from Datos import *
import copy
# Ejercicio 1) Se tiene una lista de diccionarios, donde cada diccionario representa un producto con nombre, precio y categoría. Escribe una función procesar_productos que reciba esta lista y una función de operación. Luego, crear distintas funciones para: filtrar productos de una categoría dada; calcular el precio promedio de todos los productos.
def procesar_productos(productos:list, operación:callable) -> callable:
    return operación(productos)

def filtrar_productos_categoría(filtro:str) -> callable:
    def filtrar_productos(productos:list) -> list:
        productos_filtrados = []
        for producto in productos:
            if producto["categoria"] == filtro:
                productos_filtrados.append(producto)
        return productos_filtrados
    return filtrar_productos

def calcular_promedio_precio_productos(productos:list) -> int:
    suma_precios = 0
    cantidad_precios = 0
    for producto in productos:
        suma_precios += producto["precio"]
        cantidad_precios += 1
    precio_promedio = suma_precios / cantidad_precios
    return precio_promedio

filtros_productos = {
    "tecnología": filtrar_productos_categoría("tecnología"),
    "hogar": filtrar_productos_categoría("hogar")
}
# Ejercicio 2) Se tiene una lista de diccionarios donde cada diccionario representa un estudiante con su nombre, curso y calificación. Escribe una función procesar_estudiantes que reciba esa lista y una función como parámetro. Luego, implementar: una función que devuelva solo los estudiantes aprobados (nota mayor o igual a 60), y otra que calcule el promedio de calificaciones de todos los estudiantes.
def procesar_estudiantes(estudiantes:list, función:callable) -> callable:
    return función(estudiantes)

def filtrar_estudiantes_nota(filtro:float) -> callable:
    def filtrar_estudiantes(estudiantes:list) -> list:
        estudiantes_filtrados = []
        for estudiante in estudiantes:
            if estudiante["calificacion"] >= filtro:
                estudiantes_filtrados.append(estudiante)
        return estudiantes_filtrados
    return filtrar_estudiantes

def calcular_promedio_notas_estudiantes(estudiantes:list) -> int:
    suma_notas = 0
    cantidad_notas = 0
    for estudiante in estudiantes:
        suma_notas += estudiante["calificacion"]
        cantidad_notas += 1
    nota_promedio = suma_notas / cantidad_notas
    return nota_promedio

filtros_estudiantes = {
    "aprobados": filtrar_estudiantes_nota(6.0)
}
# Ejercicio 3) Se tiene una lista de diccionarios donde cada uno representa una película con título, año y puntaje. Escribe una función procesar_peliculas que reciba esa lista y una función como parámetro. Luego, implementa: una función que devuelva las películas ordenadas por puntaje de mayor a menor, y otra función que ordene las películas por año de estreno de menor a mayor.
def procesar_películas(películas:list, función:callable) -> callable:
    return función(películas)

def copiar_lista(lista:list) -> list:
    return copy.deepcopy(lista)

def extraer_valor_diccionario(clave:str) -> callable:
    def extraer_valor(valor: dict):
        return valor[clave]
    return extraer_valor

def ordenar_películas_criterio(criterio: str, invertido: bool = False) -> callable:
    def ordenar_películas(películas:list) -> list:
        clave_ordenamiento = extraer_valor_diccionario(criterio)
        películas.sort(key=clave_ordenamiento, reverse=invertido)
        return películas
    return ordenar_películas

tipos_ordenamiento = {
    "puntaje": ordenar_películas_criterio("puntaje", invertido=True),
    "año": ordenar_películas_criterio("año")
}