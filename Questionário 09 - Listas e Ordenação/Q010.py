# Intercalar um array

n = int(input())

lista1 = []
for i in range(n):
    valor1 = int(input())
    lista1.append(valor1)

lista2 = []
for a in range(n):
    valor2 = int(input())
    lista2.append(valor2)

for b in range(n):
    print(lista1[b])
    print(lista2[b])
