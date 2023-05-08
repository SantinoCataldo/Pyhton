x = int(input("Ingrese cantidad de numeros: "))
num = 1
pares = 0
impares = 0

while num <= x:
    valor = int(input('\nIngrese valor '+str(num)+': '))
    num += 1
    if valor % 2 == 0:
        print('Es par')
        pares += 1
    else:
        print('No es par')
        impares += 1

print('\nPares:', pares, '\nImpares:', impares)

#©SantinoCataldo