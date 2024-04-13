# Quadrado e Cubo

N = int(input())

for i in range(1, N + 1):
  quadrado = (i)**2
  cubo = (i)**3

  print('{} {} {}'.format(i, quadrado, cubo))
