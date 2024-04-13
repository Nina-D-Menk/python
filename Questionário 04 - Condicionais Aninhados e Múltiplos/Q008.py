# Zerinho ou Um

A = int(input())
B = int(input())
C = int(input())

if (A == B and A == C and C == B):
  print('\n* ')

elif A != B and A != C:
  print('\nA')

elif B != A and B != C:
  print('\nB')

elif C != B and C != A:
  print('\nC')
