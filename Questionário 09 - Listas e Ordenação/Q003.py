# Desafio do maior número

numeros = input().split()
numero = []

for i in range(len(numeros)):
  numero.append(int(numeros[i]))

maior = 0
for i in range(len(numero) - 1):
  if numero[i] > numero[i + 1] and numero[i] > maior:
    maior = numero[i]

print(maior)
