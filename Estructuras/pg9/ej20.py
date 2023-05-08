suma1 = 0
suma2 = 0
x = 1

while x <= 15:
    valor = int(input('Ingrese el valor '+str(x)+' de la primer lista: '))
    suma1 += valor
    x += 1
x = 1
print('\n')
while x <= 15:
    valor = int(input('Ingrese el valor '+str(x)+' de la segunda lista: '))
    suma2 += valor
    x += 1

if suma1 > suma2:
    print('\nLa lista 1 es mayor')
elif suma1 < suma2:
    print('\nLa lista 2 es mayor')
else:
    print('\nLas listas son iguales')

print('Lista 1:', suma1, '\nLista 2:', suma2)

#©SantinoCataldo
