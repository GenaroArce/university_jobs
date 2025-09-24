"""
IndexError: cuando realiza lista1.clear() vacia la lista.
y al intentar lista1.pop() lanza error debido a que la lista esta vacia.
"""

lista1 = [7, 4, 5, 3]
lista1.append(6)
lista1[2] = 10
lista1.insert(3, 8)
lista1.remove(4)
lista1.pop(2)
lista1.extend([1, 2])
lista1.reverse()
lista1.sort()
lista1.reverse()
lista1.clear()
lista1.pop()

print(lista1)