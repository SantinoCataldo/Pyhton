sld = int(input("Ingrese sueldo:"))
ant = int(input("Ingrese antigüedad:"))

if sld < 500 and ant >= 10:
    por = sld * (20/100)
    aum = sld+por
    print('Con el aumento el sueldo es:',aum)
elif sld < 500 and ant < 10:
    por = sld * (5/100)
    aum = sld+por
    print('Con el aumento el sueldo es:',aum)
else:
    print('No cumple con los requisitos para recibir un aumento, su sueldo sigue siendo:',sld)

#©SantinoCataldo