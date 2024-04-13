# Acima da média

n0 = float(input('\n'))
n1 = float(input())
n2 = float(input())

m = (n1 + n2 + n0) / 3
n = 0

if (n0 > m):
  n = n + 1

if (n1 > m):
  n = n + 1

if (n2 > m):
  n = n + 1

print(n)
