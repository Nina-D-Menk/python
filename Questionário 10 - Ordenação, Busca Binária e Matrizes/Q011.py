# Acima ou abaixo das diagonais de uma matriz

locus = input()
limiar = int(input())
ordem = int(input())
mat = []
lista = []

for _ in range(ordem):
  linha = input().split()
  lista = []
  for j in range(len(linha)):
    lista.append(int(linha[j]))
  mat.append(lista)

soma = 0
for i in range(ordem):
  for j in range(i + 1, ordem):
    if locus == 'acima':
      soma += mat[i][j]

    else:
      soma += mat[j][i]

print(soma > limiar)
