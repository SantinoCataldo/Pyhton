preguntas = int(input('ingrese el total de preguntas: '))
correctas = int(input('ingrese el total de preguntas: '))
total = correctas*100/preguntas
print(total)
if total >= 90:
    print('Nivel maximo')
elif total >= 75 and total <= 90:
    print('Nivel medio')
elif total >= 50 and total <= 75:
    print('Nivel regular')
else:
    print('fuera de nivel')

#©SantinoCataldo