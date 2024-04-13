# Soma dos Dígitos

def SomaDigitos(n):
  n = str(n)
  soma = 0
  for i in range(len(n)):
    soma += int(n[i])

  return soma

numero = 3250 #int(input())
print(SomaDigitos(numero))
