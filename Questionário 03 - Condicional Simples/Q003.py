# Alugando um veículo

diaria = int(input('\n'))
quilometragem = int(input())

cota = diaria * 100

if quilometragem > cota and diaria > 1:
  quilometragem -= cota
  valor = diaria * 90 + quilometragem * 12
  print('{:.2f}'.format(valor))

elif quilometragem > cota and diaria == 1:
  quilometragem -= cota
  valor = 90 + quilometragem * 12
  print('{:.2f}'.format(valor))

else:
  valor = diaria * 90
  print('{:.2f}'.format(valor))
