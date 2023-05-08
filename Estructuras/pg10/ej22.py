x = int(input('Cuantos triangulos ingresara: '))
tri = 1
may = 0

for f in range(x):
    bas = int(input('\nIngrese base del triangulo '+str(tri)+': '))
    alt = int(input('Ingrese altura del triangulo '+str(tri)+': '))
    sup = (bas*alt)/2
    print('La superficie es:', sup)
    tri += 1

    if sup >= 12:
        may += 1

print('\nSuperficies > 12:', may)

#©SantinoCataldo