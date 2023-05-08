x = int(input("Ingrese cantidad de personas: "))
per = 1
suma = 0
alt = 0
baj = 0

while per <= x:
    suel = int(input('Ingrese el sueldo de la persona '+str(per)+':'))
    if suel >= 100 and suel <= 300:
        alt += 1
    elif suel > 300:
        baj += 1
    suma += suel
    per += 1

print('\nSueldos 100-300:', alt, '\nSueldos > 300:', baj,
      '\nEl importe que gasta la empresa en sueldos al personal es de:', suma)

#©SantinoCataldo