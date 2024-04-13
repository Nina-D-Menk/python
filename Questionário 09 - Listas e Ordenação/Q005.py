# Iguais a n

lista = []
N = 0

for _ in range(101):
  N = int(input())
  lista.append(N)

for i in range(100):
  if lista[i] == N:
    print(i)
