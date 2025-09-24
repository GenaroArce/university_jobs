"""
Genera cuatro numeros aleatorios y calcula el promedio
"""

import random

lista_numeros = []
for i in range(0, 10):
    lista_numeros.append(random.randint(1,10))

print(lista_numeros)

sumar = 0

for i in lista_numeros:
    sumar += i

promedio = sumar / len(lista_numeros) 

print(f"El promedio de los numeros: {promedio}")