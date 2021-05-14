#Ejercicio 5

"""
Resuelva el ejercicio de 3 de la guía uno aplicando el filtro para los CV.
"""
"""
El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto vacante, 
el requisito mínimo es la edad, pero en los datos solo tienen la fecha denacimiento.
"""

nacimiento = int (input("Ingrese el año de nacimiento: "))

año = int (input ("Ingrese el año actual: "))

edad = año - nacimiento

if (edad >=25):
    print ("El postulante es apto")
else:
    print ("El postulante no es apto")
