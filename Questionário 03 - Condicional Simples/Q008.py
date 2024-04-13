# Ano Bissexto

Ano = int(input('\n'))

if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
  print('BISSEXTO')

else:
  print('NAOBISSEXTO')
