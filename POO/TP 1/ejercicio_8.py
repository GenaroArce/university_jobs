valorInicial = int(input("Ingrese el valor inicia > "))
valorFinal = int(input("Ingrese el valor final > "))
salto = int(input("Ingrese el valor de salto > "))

while valorInicial <= valorFinal:
    print(valorInicial, end=" ")
    valorInicial += salto

for valor in range(valorInicial, valorFinal + 1, salto):
    print(valor, end=" ")