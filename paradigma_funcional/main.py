from Funciones import *
# Ejericicio 1) Se tiene una lista de diccionarios, donde cada diccionario representa un producto con nombre, precio y categoría. Escribe una función procesar_productos que reciba esta lista y una función de operación. Luego, crear distintas funciones para: filtrar productos de una categoría dada; calcular el precio promedio de todos los productos.
productos_tecnología = procesar_productos(productos, filtros_productos["tecnología"])
print(f"\nLista de productos dentro de la categoría \"Tecnología\":")
for producto in productos_tecnología:
      print(f"- {producto["nombre"]}")

productos_hogar = procesar_productos(productos, filtros_productos["hogar"])
print(f"\nLista de productos dentro de la categoría \"Hogar\":")
for producto in productos_hogar:
      print(f"- {producto["nombre"]}")

promedio_precios = procesar_productos(productos, calcular_promedio_precio_productos)
print(f"\nEl promedio de precios de todos los productos es de {promedio_precios:.2f} pesos")

# Ejercicio 2) Se tiene una lista de diccionarios donde cada diccionario representa un estudiante con su nombre, curso y calificación. Escribe una función procesar_estudiantes que reciba esa lista y una función como parámetro. Luego, implementar: una función que devuelva solo los estudiantes aprobados (nota mayor o igual a 60), y otra que calcule el promedio de calificaciones de todos los estudiantes.
estudiantes_aprobados = procesar_estudiantes(estudiantes, filtros_estudiantes["aprobados"])
print(f"\nLista de estudiantes aprobados (nota 6 o más):")
for estudiante in estudiantes_aprobados:
      print(f"- {estudiante["nombre"]}")

promedio_notas = procesar_estudiantes(estudiantes, calcular_promedio_notas_estudiantes)
print(f"\nEl promedio de notas de todos los estudiantes es de {promedio_notas:.2f} puntos")

# Ejercicio 3) Se tiene una lista de diccionarios donde cada uno representa una película con título, año y puntaje. Escribe una función procesar_peliculas que reciba esa lista y una función como parámetro. Luego, implementa: una función que devuelva las películas ordenadas por puntaje de mayor a menor, y otra función que ordene las películas por año de estreno de menor a mayor.
copia_películas = copiar_lista(peliculas)
películas_ordenadas_puntaje = procesar_películas(copia_películas, tipos_ordenamiento["puntaje"])
print(f"\nLista de péliculas ordenadas por puntaje de mayor a menor:")
for película in películas_ordenadas_puntaje:
      print(f"- {película["titulo"]} ({película["puntaje"]})")

películas_ordenadas_año = procesar_películas(copia_películas, tipos_ordenamiento["año"])
print(f"\nLista de péliculas ordenadas por año de estreno de menor a mayor:")
for película in películas_ordenadas_año:
      print(f"- {película["titulo"]} ({película["año"]})")