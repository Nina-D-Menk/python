# Critério do Seguro

homen = int(input('\n'))
idade_40 = int(input())

if homen == 1 and idade_40 == 1 or homen == 1 and idade_40 == 0:
  print('0')

elif homen == 0 and idade_40 == 1:
  print('1')

else:
  print('0')
