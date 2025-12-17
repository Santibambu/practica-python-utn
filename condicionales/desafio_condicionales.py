MetrosCúbicos = int(input("Ingrese la cantidad de metros cúbicos de agua que ha consumido este mes\n"))
TipoCliente = int(input("Ingrese el tipo de cliente que usted es:\n1) Residencial\n2) Comercial\n3) Industrial\n"))

FacturaBase = 7000 + (MetrosCúbicos * 200)
Bonificación = 0
Recargo = 0

if TipoCliente == 1:
    if FacturaBase <= 35000:
        Bonificación = FacturaBase * .05
    if MetrosCúbicos <= 30:
        Bonificación = FacturaBase * .10
    elif MetrosCúbicos >= 80:
        Recargo = FacturaBase * .15
elif TipoCliente == 2:
    if MetrosCúbicos >= 150:
        Bonificación = FacturaBase * .08
    elif MetrosCúbicos >= 300:
        Bonificación = FacturaBase * .12
    elif MetrosCúbicos <= 50:
        Recargo = FacturaBase * .05
elif TipoCliente == 3:
    if MetrosCúbicos >= 500:
        Bonificación = FacturaBase * .20
    elif MetrosCúbicos >= 1000:
        Bonificación = FacturaBase * .30
    elif MetrosCúbicos <= 200:
        Recargo = FacturaBase * .10

FacturaSubtotal = FacturaBase - Bonificación + Recargo
FacturaIVA = FacturaSubtotal * 0.21
FacturaFinal = FacturaSubtotal + FacturaIVA

print(f"La factura base de su consumo de agua es de {FacturaBase} pesos")
if Bonificación > 0:
    print(f"Por su consumo y tipo de cliente obtuvo un descuento del {(Bonificación / FacturaBase) * 100}%")
elif Recargo > 0:
    print(f"Por su consumo y tipo de cliente le aplicamos un recargo del {(Recargo / FacturaBase) * 100}%")
print(f"El subtotal de la factura es de {FacturaSubtotal} pesos")
print(f"La factura con IVA del 21% aplicado es de {FacturaIVA} pesos")
print(f"La factura final a pagar es de {FacturaFinal} pesos")