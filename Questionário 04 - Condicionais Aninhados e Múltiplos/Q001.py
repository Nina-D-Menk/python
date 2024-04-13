# Quantidade de dias de um mês/ano

mes = int(input('\n'))
ano = int(input())

meses_31 = {1, 3, 5, 7, 8, 10, 12}
meses_30 = {4, 6, 9, 11}
# {} = Conjunto

if mes == 2:
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('29')

  else:
    resultado = 28
    print('28')

elif mes in meses_30:
  resultado = 30
  print('30')

elif mes in meses_31:
  resultado = 31
  print('31')
