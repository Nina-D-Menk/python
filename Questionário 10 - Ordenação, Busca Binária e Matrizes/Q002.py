# Brincando com matrizes

matriz = []
for _ in range(3):
  lista = []
  for _ in range(3):
    linha = int(input())
    lista.append(linha)

  matriz.append(lista)


soma = 0
maior_valor = float(matriz[0][0])
diagonal= 0
for i in range(3):
  for j in range(3):
    soma += matriz[i][j]
    if matriz[i][j] > maior_valor:
        maior_valor = matriz[i][j]

    if i == j:
        diagonal += matriz[i][j]

media = soma / 9
if maior_valor > 0:
    delta = 1

elif maior_valor < 0:
    delta = -1

else:
  delta = 0


print("{:.2f}".format(media), end=' ')
print(int(maior_valor), end=' ')
print(int(delta), end=' ')
print(int(diagonal))
