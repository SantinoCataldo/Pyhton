x=int(input("Ingrese el valor de X:"))
y=int(input("Ingrese el valor de Y:"))

if x >= 0 and y>=0 :
    print('El valor x=',x,'y=',y,'esta en el primer cuadrante')
elif  x <= 0 and y >= 0:
    print('El valor x=',x,'y=',y,'esta en el segundo cuadrante')
elif  x <= 0 and y <= 0:
    print('El valor x=',x,'y=',y,'esta en el tercer cuadrante')
elif  x >= 0 and y <= 0:
    print('El valor x=',x,'y=',y,'esta en el cuarto cuadrante')    

#©SantinoCataldo