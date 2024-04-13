# Contar um caracter na string
#.count(): função para contar parmentros

contado = str(input()).lower()
caracter = str(input().lower())

total = 0
for i in range(len(contado)):

    if contado[i] == caracter:
        total += 1

print(total)
