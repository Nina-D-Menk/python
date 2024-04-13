# Classificação no Mundial

pontos= [int(input()) for i in range(6)]

pontuacao_total = sum(pontos)

if pontuacao_total >= 100:
  print('Classificado')

else:
  print('Eliminado')
