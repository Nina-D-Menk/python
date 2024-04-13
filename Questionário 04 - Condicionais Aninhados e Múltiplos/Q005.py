# Conceito MEC

livros = int(input())
alunos = int(input())

razão = alunos / livros

if razão <= 8:
  res = 'A'
  print(res)

elif razão >= 9 and razão <= 12:
   res = 'B'
   print(res)

elif razão >= 12 and razão <= 18:
   res = 'C'
   print(res)

elif razão > 18:
  res = 'D'
  print(res)
