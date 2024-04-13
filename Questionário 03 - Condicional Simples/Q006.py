# Menor de 3

x = int(input('\n'))
y = int(input())
z = int(input())

if x <= y and x <= z:
  print(x)

elif y <= x and y <= z:
  print(y)

else:
  print(z)
