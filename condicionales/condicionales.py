# Ejercicio 1

AlturaJugador = int(input("Porfavor, ingrese su altura\n"))
if AlturaJugador <= 160:
    print("Su poisición en la cancha es Base")
elif AlturaJugador <= 179:
    print("Su poisición en la cancha es Escolta")
elif 180 <= AlturaJugador <= 199:
    print("Su poisición en la cancha es Alero")
elif AlturaJugador >= 200:
    print("Su poisición en la cancha es Pívot")

# Ejercicio 2

import random

Nota = random.randint(1, 10)

if 1 <= Nota <= 3:
    print(f"Desaprobado, la nota es {Nota}")
elif Nota == 4 or Nota == 5:
    print(f"Aprobado, la nota es {Nota}")
else:
    print(f"Promoción directa, la nota es {Nota}")