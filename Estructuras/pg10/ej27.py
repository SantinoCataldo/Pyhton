valor = int(input('Cuantos puntos ingresara: '))
inc = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for f in range(valor):
    x = int(input('\nIngrese el valor de X del punto '+str(inc)+': '))
    y = int(input('Ingrese el valor de Y del punto '+str(inc)+': '))
    inc += 1

    if x >= 0 and y >= 0:
        print('Esta en el primer cuadrante')
        c1 += 1
    elif x <= 0 and y >= 0:
        print('Esta en el segundo cuadrante')
        c2 += 1
    elif x <= 0 and y <= 0:
        print('Esta en el tercer cuadrante')
        c3 += 1
    elif x >= 0 and y <= 0:
        print('Esta en el cuarto cuadrante')
        c4 += 1

print('\nCuadrante 1: ', c1, '\nCuadrante 1: ', c2,
      '\nCuadrante 1: ', c3, '\nCuadrante 4: ', c4)

#©SantinoCataldo