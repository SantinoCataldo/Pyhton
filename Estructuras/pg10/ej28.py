pos = 0
neg = 0
m15 = 0
par = 0
x = 1

for f in range(10):
    val = int(input('\nIngrese el valor '+str(x)+': '))
    if val < 0:
        neg += 1
        print('Negativo')
    elif val > 0:
        pos += 1
        print('Positivo')
    if val % 15 == 0:
        m15 += 1
        print('Multiplo de 15')
    if val % 2 == 0:
        par += 1
        print('Par')
    x += 1

print('\nPositivos:', pos, '\nNegativos:', neg,
      '\nMultiplos de 15:', m15, '\nPares:', par)

#©SantinoCataldo