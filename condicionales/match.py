Viajar = True

ConfirmaciónViaje = input("¿Desea planificar sus viajes según la estación del año? (S/N)\n").upper()
if ConfirmaciónViaje == "S":
    print("Se viaja")
elif ConfirmaciónViaje == "N":
    print("No se viaja")
    Viajar = False
else:
    Viajar = False
    
if Viajar == True:
    Estación = int(input("¿En qué estación desea viajar?\n1) Verano\n2) Otoño\n3) Invierno\n4) Primavera\n"))
    match Estación:
        case 1: print("Puede viajar a Mar del PLata y Cataratas")
        case 2: print("Puede viajar a todos los lugares")
        case 3: print("Puede viajar a Bariloche")
        case 4: print("Puede viajar a todos los lugares, excepto Bariloche")