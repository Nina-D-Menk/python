# Remover caracteres de uma string

string1 = str(input())
string2 = str(input())
lista = []

for i in range(len(string1)):
  if string1[i] not in string2:
    lista.append(string1[i])

string_resultante = ''.join(lista)
print(string_resultante)
