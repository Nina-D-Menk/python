# Sequência de 10

N = input().split()
lista = []
contador = 0

for i in range(len(N)):
    lista.append(int(N[i]))

ultimo = lista[len(lista) - 1]
for i in range(len(lista)):
    if lista[i] == ultimo:
        contador += 1

print('O numero {} apareceu {} vezes'.format(ultimo, contador))
