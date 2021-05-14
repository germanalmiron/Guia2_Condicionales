#Ejercicio 22

"""

Simular que una persona tira tres veces un dado de seis lados (de manera aleatoria),
determinar si la persona saco un 5 y cuantos suma el total de los tres tiros.

"""

tiro_1 = int(input("Ingrese el valor del dado del primer tiro: "))
tiro_2 = int(input("Ingrese el valor del dado del segundo tiro: "))
tiro_3 = int(input("Ingrese el valor del dado del tercer tiro: "))

if(tiro_1 == 5 or tiro_2 ==5 or tiro_3 == 5):
    print("Sacó al menos un 5")

else:
    print("No sacó un 5")
print("La suma total de los tres tiros es ", tiro_1 + tiro_2 + tiro_3)
