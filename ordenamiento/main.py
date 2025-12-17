from Funciones import *

# Ejercicio 1) Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente
Nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

NombresOrdenados = OrdenarNombres(Nombres)
for i in range(len(NombresOrdenados)):
    print(NombresOrdenados[i])

# Ejercicio 2) Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente
Nombres = ["Matematica", "Investigacion Operativa", "Ingles", "Literatura", "Ciencias Sociales", "Computacion", "Ingles", "Algebra", "Contabilidad", "Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100, 98, 56, 25, 87, 38, 64, 42, 28, 91, 66, 35, 49, 57, 98]

MateriasOrdenadas = OrdenarMaterias(Nombres, Puntos)
for i in range(len(MateriasOrdenadas)):
    print(MateriasOrdenadas[i])

# Ejercicio 3) Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]
Nota = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10, 4, 8]

EstudiantesOrdenados = OrdenarEstudiantes(Estudiantes, Apellidos, Nota)
for fila in zip(*EstudiantesOrdenados):
    print(f"{fila[0]:<10} {fila[1]:<10} {fila[2]}")

# Ejercicio 4) 
MostrarMenúOpciones()