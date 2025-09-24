"""
Determinar si un numero es PAR o IMPAR
"""

numero = 5

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

"""
numero ingresado por el usuario verificar si es multiplo de 4
multiplo de 3
and o or
divisor de 36
"""
numero_usuario = int(input("Ingrese un numero: "))

if numero_usuario % 4 == 0:
    print("Es multiplo de 4")
elif numero_usuario % 3 == 0 and 36 % numero_usuario == 0:
    print("Es multiplo de 3 y divisor de 36")
elif numero_usuario % 3 == 0 or 36 % numero_usuario == 0:
    print("Es multiplo de 3 o divisor de 36")
else:
    print("No es multiplo de 4, ni multiplo de 3, ni divisor de 36.")