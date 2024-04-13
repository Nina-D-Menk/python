# Sedex

N = int(input('\n'))
A, L, P = input().split()

A = int(A)
L = int(L)
P = int(P)

if min(A, L, P) >= N:
  print('S')

else:
  print('N')
