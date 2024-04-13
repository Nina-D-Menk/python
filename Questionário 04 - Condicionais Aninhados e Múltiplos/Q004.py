# Classificação de Triângulos

a = float(input('\n'))
b = float(input())
c = float(input())

if a == b and a == c:
   print('equilatero')

elif a != b and a != c and c != b:
  print('escaleno')

else:
  print('isosceles')
