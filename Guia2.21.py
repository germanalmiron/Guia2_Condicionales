#Ejercicio 21

"""
Dado 5 números sumar los que son múltiplos de dos y obtener el promedio de estos.

"""
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))
num4 = int(input('Ingrese un número: '))
num5 = int(input('Ingrese un número: '))

cantidad_multiplos_2 = 0
suma = 0

if(num1 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num1
if(num2 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num2
if(num3 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num3
if(num4 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num4
if(num5 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num5

print('La cantidad de Múltiplos de 2 son: ', cantidad_multiplos_2)
print('El promedio de los Múltiplos de 2 son: ', suma / cantidad_multiplos_2)















