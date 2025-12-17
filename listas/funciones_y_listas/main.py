from Funciones import *
from listas_personas import nombres

# Ejercicio 1
Nombres = PedirListaNombres()

for i in range(len(Nombres)):
    print(Nombres[i])

# Ejercicio 2
Números = PedirListaNúmeros()

for i in range(len(Números)):
    print(Números[i])

# Ejercicio 3
NúmerosEnRango = PedirListaNúmerosEnRango()

for i in range(len(NúmerosEnRango)):
    print(NúmerosEnRango[i])

# Ejercicio 4
ListaNúmeros = [random.randint(1, 100) for _ in range(50)]
NúmeroAEncontrar = random.randint(1, 100)

print(EncontrarNúmeroEnLista(ListaNúmeros, NúmeroAEncontrar))

# Ejercicio 5
Edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]
Nombres = EncontrarPersonaMenor(Edades)
EdadMenor = float("inf")

for i in range(len(Edades)):
    if Edades[i] <= EdadMenor:
        EdadMenor = Edades[i]

print(f"Las personas con menor edad tienen {EdadMenor} años. Ellos son:")
for i in range(len(Nombres)):
    print(Nombres[i])

# Ejercicio 6
MostrarNombres(nombres)

# Ejercicio 7 y 8
MostrarMenúOpciones()