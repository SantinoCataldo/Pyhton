sum1 = 0
sum2 = 0
sum3 = 0
x = 1
for f in range(5):
    edad = int(input('Ingrese la edad del alumno '+str(x)+' turno mañana: '))
    sum1 += edad
    prom1 = sum1/5
    x += 1
print('\nPromedio de edad turno mañana=', round(prom1, 2))
x = 1

for f in range(6):
    edad = int(input('Ingrese la edad del alumno '+str(x)+' turno tarde: '))
    sum2 += edad
    prom2 = sum2/6
    x += 1
print('\nPromedio de edad turno tarde=', round(prom2, 2))
x = 1

for f in range(11):
    edad = int(input('Ingrese la edad del alumno '+str(x)+' turno noche: '))
    sum3 += edad
    prom3 = sum3/11
    x += 1
print('\nPromedio de edad turno noche=', round(prom3, 2))

if prom1 > prom2 and prom1 > prom3:
    print('\nEl mayor promedio es:', round(prom1, 2), 'del turno mañana')
elif prom2 > prom3:
    print('\nEl mayor promedio es:', round(prom2, 2), 'del turno tarde')
else:
    print('\nEl mayor promedio es:', round(prom3, 2), 'del turno noche')

#©SantinoCataldo