import random
num = random.randint(0, 100)
intentos = 0

while True:
    print('\nBienvenido al juego de adivinar el numero')
    print('Tenes que adivinar un numero del 1 y 100 ¿Podes hacerlo?')
    print('\nPero primero tenes que elegir un nivel de dificultad')
    print('1:Facil -- 2:Medio -- 3:Dificil -- 4:Imposible')
    eleccion = int(input("Seleccione la dificultad con un número de opción: "))

    match eleccion:
        case 1:
            print('\nNivel 1 (Facil): tenes que adivinar el numero, pero vas a tener mucha ayuda')
            while True:
                intentos += 1
                x = int(input('\nAdivine el numero entre el 1 y el 100: '))
                res = x-num
                if (x == num):
                    print(f'\nLo lograste el numero era {num}, Felicitaciones')
                    break
                elif res <= 10 and res > 0:
                    print(f'Te pasaste muy poco (1-10)')
                elif res >= 11 and res <= 20:
                    print('Te pasate un poco (10-20)')
                elif res >= 21:
                    print('Te pasaste mucho (>20)')
                elif res >= -10 and res < 0:
                    print(f'Te falta muy poco(1-10)')
                elif res <= -11 and res >= -20:
                    print('Te falta poco (10-20)')
                elif res <= -21:
                    print('Te falta mucho (>20)')
            print(f'\nTuviste una cantidad de {intentos} intentos')
            break
        case 2:
            print('\nNivel 2 (Medio): tenes que adivinar el numero, pero vas a tener un poco de ayuda')
            intentos = 0
            while True:
                intentos += 1
                x = int(input('\nAdivine el numero entre el 1 y el 100: '))
                if (x == num):
                    print(f'\nLo lograste el numero era {num}, Felicitaciones')
                    break
                elif x < num:
                    print("Te falta para llegar al numero")
                elif x > num:
                    print('Te pasaste del numero')
            print(f'\nTuviste una cantidad de {intentos} intentos')
            break
        case 3:
            print('\nNivel 3 (Dificil): tenes que adivinar el numero, pero vas a tener un poco de ayuda y 5 intentos')
            intentos = 0
            while True:
                intentos += 1
                x = int(input('\nAdivine el numero entre el 1 y el 100: '))
                if (x == num):
                    print(f'\nLo lograste el numero era {num}, Felicitaciones')
                    break
                if intentos == 5:
                    print(
                        f'\nFallaste el numero era {num}')
                    break
                elif x < num:
                    print("Te falta para llegar al numero")
                elif x > num:
                    print('Te pasaste del numero')
            print(f'\nTuviste una cantidad de {intentos} intentos')
            break
        case 4:
            print('\nNivel 4 (Imposible): tenes que adivinar el numero, pero vas a tener mucha ayuda y 2 intentos')
            intentos = 0
            while True:
                intentos += 1
                x = int(input('\nAdivine el numero entre el 1 y el 100: '))
                res = x-num
                if (x == num):
                    print(f'\nLo lograste el numero era {num}, Felicitaciones')
                    break
                if intentos == 2:
                    print(f'\nFallaste el numero era {num}')
                    break
                elif res <= 10 and res > 0:
                    print(f'Te pasaste muy poco (1-10)')
                elif res >= 11 and res <= 20:
                    print('Te pasate un poco (10-20)')
                elif res >= 21:
                    print('Te pasaste mucho (>20)')
                elif res >= -10 and res < 0:
                    print(f'Te falta muy poco (1-10)')
                elif res <= -11 and res >= -20:
                    print('Te falta poco (10-20)')
                elif res <= -21:
                    print('Te falta mucho (>20)')
            print(f'\nTuviste una cantidad de {intentos} intentos')
            break

        #SantinoCataldo