# Garantia Estendida

a = float(input('\n'))
b = int(input())

if b == 0:
  print('{:.2f}'.format(a))

elif b == 1:
  garantia = a * 1.03
  print('{:.2f}'.format(garantia))

elif b == 2:
  garantia = a * 1.05
  print('{:.2f}'.format(garantia))
