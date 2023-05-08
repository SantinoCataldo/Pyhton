x = int(input('Cuantos triangulos ingresara: '))
tri = 1
equi = 0
esca = 0
isos = 0

for f in range(x):
    lad1 = int(input('\nIngrese primer lado del triangulo '+str(tri)+': '))
    lad2 = int(input('Ingrese segundo lado del triangulo '+str(tri)+': '))
    lad3 = int(input('Ingrese tercer lado del triangulo '+str(tri)+': '))
    tri += 1
    if lad1 == lad2 and lad1 == lad3:
        print('Es un triangulo equilátero')
        equi += 1
    elif lad1 != lad2 and lad1 != lad3:
        print('Es un triangulo escaleno')
        esca += 1
    else:
        print('Es un triangulo isosceles')
        isos += 1

print('\nTriangulos equilateros:', equi, '\nTriangulos escalenos:',
      esca, '\nTriangulos isosceles:', isos)

#©SantinoCataldo