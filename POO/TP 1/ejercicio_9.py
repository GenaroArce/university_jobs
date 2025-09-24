valores = []
pregunta = True

while pregunta:
    numero_entero = int(input("Ingrese el valor: "))

    while numero_entero <= 0:
        print("No puedes ingresar valores negativos, intente nuevamente")
        numero_entero = int(input("Ingrese el valor: "))

    valores.append(numero_entero)

    pregunta_string = input("Quieres seguir ingresando valores? s/n ")
    pregunta = False if pregunta_string != "s" else True

suma = 0
menor = valores[0]
mayor = valores[0]

for i in valores:
    suma += i
    
    if i < menor:
        menor = i

    if i > mayor:
        mayor = i

print(f"Promedio: {suma / len(valores)}")
print(f"Cantidad de valores: {len(valores)}")
print(f"Valor mayor: {mayor}")
print(f"Valor menor: {menor}")