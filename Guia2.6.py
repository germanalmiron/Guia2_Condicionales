#Ejercicio 6

"""
Dado dos números determinar cuál es el mayor o si son iguales.
"""

numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número:  '))

# Opción 1

if(numero_1 > numero_2):
    print('El primer número es mayor que el segundo número: ')

elif    (numero_2 > numero_1):
        print('El segundo número es mayor que el primer número: ')

else:
    print("Son iguales")

print('fin del algoritmo')

# Opcion 2
# if(numero_1 > numero_2):
#     print('el número A es mayor que el numero B')
# else:
#     if(numero_2 > numero_1):
#         print('el número B es mayor que el numero A')
#     else:
#         print("son iguales")
# print('fin del algoritmo')
