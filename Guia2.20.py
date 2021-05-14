#Ejercicio 20

"""
Dado 5 números contar cuantos son múltiplos de 3.

"""
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))
num4 = int(input('Ingrese un número: '))
num5 = int(input('Ingrese un número: '))

cantidad_multiplos_3 = 0

if(num1 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num2 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num3 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num4 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num5 % 3 == 0):
    cantidad_multiplos_3 += 1

print('La cantidad de multiplos de 3 son: ', cantidad_multiplos_3)










