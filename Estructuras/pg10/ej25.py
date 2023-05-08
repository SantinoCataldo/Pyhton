x = int(input('Ingrese un numero del 1-10: '))

for f in range(3):
    if x > 10:
        x = int(input('Ingrese un numero del 1-10: '))
    else:
        for f in range(x, x*13, x):
            print(f)

#©SantinoCataldo