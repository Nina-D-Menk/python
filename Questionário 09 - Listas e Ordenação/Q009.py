# Menor Valor e Posição

N = int(input())
lista = input().split()
numero = []

for i in range(N):
  numero.append(int(lista[i]))

menor = numero[0]
posicao = 0
for i in range(1, N - 1):
  if numero[i + 1] < numero[i] and numero[i + 1] < menor:
    menor = numero[i + 1]
    posicao = i + 1

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))
