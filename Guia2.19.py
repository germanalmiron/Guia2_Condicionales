#Ejercicio 19

"""
Dado tres números mostrarlos en orden ascendente.

"""
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

if(numero_1 > numero_2 and numero_2 > numero_3):
    print("Se ordenan los números en forma ascendente: ", numero_3, numero_2, numero_1)

elif(numero_1 > numero_3 and numero_3 > numero_2):
    print("Se ordenan los números en forma ascendente: ", numero_2, numero_3, numero_1)

elif(numero_2 > numero_1 and numero_1 > numero_3):
    print("Se ordenan los números en forma ascendente: ", numero_3, numero_1, numero_2)

elif(numero_2 > numero_3 and numero_3 > numero_1):
    print("Se ordenan los números en forma ascendente: ", numero_1, numero_3, numero_2)

elif(numero_3 > numero_1 and numero_1 > numero_2):
    print("Se ordenan los números en forma ascendente: ", numero_2, numero_1, numero_3)
    
else:
    print("Se ordenan los números en forma ascendente: ", numero_1, numero_2, numero_3)

