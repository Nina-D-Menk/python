#  Média dos alunos

x = float(input('\n'))
y = float(input())
z = float(input())

med = (x + y + z) / 3

if med >= 7:
  print('\naprovado')

elif med < 3:
  print('\nreprovado')

elif med >= 3 and med < 7:
  print('\nprova final')
