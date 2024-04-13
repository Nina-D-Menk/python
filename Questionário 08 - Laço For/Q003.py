# Investimento

C, i, X = input().split()

C, i, X = float(C), float(i), int(X)

for _ in range(4 * X):
  M = C*(1 + i)**1
  R = M - C
  print('Rendimento: {:.2f} Montante: {:.2f}'.format(R, M))
  C = M
