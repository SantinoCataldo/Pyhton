alu = 1
apr = 0
des = 0

while alu <= 10:
    nota = int(input('Ingrese la nota del alumno '+str(alu)+':'))
    if nota >= 7:
        apr += 1
    else:
        des += 1
    alu += 1

print('Alumnos aprobados:', apr, '\nAlumnos desaprobados:', des)

#©SantinoCataldo