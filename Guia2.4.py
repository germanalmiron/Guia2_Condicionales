#Ejercicio 4

"""
Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
mismo está aprobado o desaprobado.
"""

nota1 = float (input ("Ingrese la nota 1: "))
nota2 = float (input ("Ingrese la nota 2: "))
nota3 = float (input ("Ingrese la nota 3: "))

nota_final = round ((nota1 + nota2 + nota3 / 3), 2)

if (nota_final > 7):
    print ("El alumno esta aprobado: ")
else:
    print ("El alumno esta desaprobado ")
