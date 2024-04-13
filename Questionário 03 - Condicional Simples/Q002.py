# Algarismo da casa das unidades

n = int(input('\n'))

if n < 0:
  n *= -1
  m = n % 10
  m *= -1
  print(m)

else:
  m = n % 10
  print(m)

# sum() explicitamente, somando os valores em um loop (como uma lista)
# map() em Python é usada para aplicar uma função a todos os itens em uma sequência (como uma lista)
# min() é usado para encontrar o menor de uma lista
# abs() em Python retorna o valor absoluto de um número
# x *= y é o mesmo que x = x * y
