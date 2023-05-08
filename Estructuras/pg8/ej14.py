num1 = int(input("Ingrese primer valor:"))
num2 = int(input("Ingrese segundo valor:"))
num3 = int(input("Ingrese tercer valor:"))
print("El mayor es:")

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

print("\nEl menor es:")

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num3:
    print(num2)
else:
    print(num3)

#©SantinoCataldo