print("Bienvenidos a la encuesta de empleados de UTN Technologies. A continuación, ingresen los datos pedidos para continuar con la encuesta.")

MasculinosAdultosSinRealidades = 0
EmpleadosSinInteligenciaArtifical = 0
MasculinoMayor = 0
NombreMayor = ""
TecnologíaMayor = ""

for i in range (10):
    NombreEmpleado = input("Ingrese su nombre.\n")

    EdadEmpleado = int(input("Ingrese su edad.\n"))
    while EdadEmpleado < 18:
        EdadEmpleado = int(input("La edad ingresada no puede ser meenor a 18 años. Vuelva a ingresar su edad.\n"))

    GéneroEmpleado = int(input("Ingrese su género:\n1) Masculino\n2) Femenino\n3) Otro\n"))
    while GéneroEmpleado not in [1, 2, 3]:
        GéneroEmpleado = int(input("El género ingresado no está dentro de nuestros parámetros. Porfavor, vuelva a ingresar su género\n"))
    match GéneroEmpleado:
        case 1: GéneroEmpleado = "Masculino"
        case 2: GéneroEmpleado = "Femenino"
        case 3: GéneroEmpleado = "Otro"

    TecnologíaEmpleado = int(input("Ingrese la tecnología en la cual se especializa:\n1) IA\n2) RV/RA\n3) IOT\n"))
    while TecnologíaEmpleado not in [1, 2, 3]:
        TecnologíaEmpleado = int(input("La tecnología ingresada es inexistente. Porfavor, vuelva a ingresar la tecnología en la que se especializa\n"))
    match TecnologíaEmpleado:
        case 1: TecnologíaEmpleado = "Inteligencia Artifical"
        case 2: TecnologíaEmpleado = "Realidad Virtual/Realidad Aumentada"
        case 3: TecnologíaEmpleado = "Internet de las Cosas"

    if GéneroEmpleado == "Masculino":
        if 25 <= EdadEmpleado <= 50:
            if TecnologíaEmpleado == "Inteligencia Artifical" or TecnologíaEmpleado == "Internet de las Cosas":
                MasculinosAdultosSinRealidades += 1

    if GéneroEmpleado != "Femenino" and TecnologíaEmpleado != "Inteligencia Artifical":
        EmpleadosSinInteligenciaArtifical += 1
    if 33 <= EdadEmpleado <= 40 and TecnologíaEmpleado != "Inteligencia Artifical":
        EmpleadosSinInteligenciaArtifical += 1

    if GéneroEmpleado == "Masculino" and EdadEmpleado > MasculinoMayor:
        MasculinoMayor = EdadEmpleado
        NombreMayor = NombreEmpleado
        TecnologíaMayor = TecnologíaEmpleado

PorcentajeEmpleadosSinInteligenciaArtifical = (EmpleadosSinInteligenciaArtifical / 10) * 100

print(f"De todos los empleados encuestados, {MasculinosAdultosSinRealidades} empleados masculinos de entre 25 y 50 años votaron por Inteligencia Artifical o Internet de las Cosas")
print(f"De todos los empleados encuestados, un {PorcentajeEmpleadosSinInteligenciaArtifical}% de los empleados no femeninos o entre 33 y 40 años no votaron por Inteligencia Artificial")
print(f"De todos los empleados masculinos encuestados, el mayor de todos es {NombreMayor}, de {MasculinoMayor} años de edad, especializado en {TecnologíaMayor}")