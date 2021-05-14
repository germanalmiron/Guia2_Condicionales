#Ejercicio 13

"""
Dado tres números obtener el mayor de estos.

"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input('Ingrese el tercer número: '))

if(numero_1 > numero_2 and numero_1 > numero_3):
    print("El número mayor es: ", numero_1)
elif(numero_2 > numero_1 and numero_2 > numero_3):
    print("El número mayor es: ", numero_2)
else:
    print("El número mayor es: ", numero_3)

