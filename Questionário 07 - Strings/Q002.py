# Buracos no texto

casos = int(input())

for _ in range(casos):
  texto = str(input().upper())

  buraco_1 = ['A', 'D', 'O', 'P', 'Q', 'R']

  buracos = 0
  for i in range(len(texto)):
    if texto[i] == 'B':
      buracos += 2
    for j in range(len(buraco_1)):
      if texto[i] == buraco_1[j]:
        buracos += 1

  print(buracos)
