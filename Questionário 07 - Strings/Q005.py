# Palíndromo
# .replace(" ", ""): substitui caracter em um input

casos = int(input())

for _ in range(casos):
  texto = input().lower().replace(" ", "")
  if texto == texto[::-1]:
    print('SIM')

  else:
    print('NAO')
