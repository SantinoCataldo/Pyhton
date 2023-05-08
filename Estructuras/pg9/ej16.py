x = int(input("Ingrese cantidad de personas: "))
per = 1
suma = 0

while per <= x:
    alt = float(input('Ingrese la altura en metros de la persona '+str(per)+':'))
    suma += alt
    per += 1

prom = suma/x
print('\nLa altura promedio es:', prom)

#©SantinoCataldo