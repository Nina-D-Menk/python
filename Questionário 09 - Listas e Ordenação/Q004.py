# Brincando com Arrays

N = int(input())
numeros = input().split()
lista = []

for i in range(N):
  lista.append(int(numeros[i]))

print(*lista[::-1])
print(*(lista[1:] + [lista[0]]))
print(*sorted(lista, reverse=True))
