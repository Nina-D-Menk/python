# Entrada e Saída CPF

CPF = input().split('.')

i = 0
for i in range(len(CPF)-1):
  print(CPF[i])

CPF = CPF[i + 1].split('-')
for i in range(len(CPF)):
  print(CPF[i])

