#Ejercicio 17

"""
Dado dos números mostrar la diferencia entre el mayor y el menor.

"""

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

if(numero_1 > numero_2):
    print("La diferencia del número es: ", numero_1 - numero_2)

elif(numero_1 < numero_2):
    print("La diferencia del número es: ", numero_2 - numero_1)

else:
    print("Los números son iguales, no hay diferencia")











