# Contagem progressiva (função sem devolução)

def Contagem_progressiva(n):
  for _ in range(1, n):
    print(n, end='-')

  print(n)
n = abs(int(input()))

for i in range(1, n + 1):
  Contagem_progressiva(i)
