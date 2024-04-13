# Quantos números são maiores ou menores que uma variação da média?

N = int(input())
lista_nota = []

for _ in range(N):
    nota = float(input())
    lista_nota.append(nota)

media = 0
for i in range(len(lista_nota)):
    media += lista_nota[i]
media = media / len(lista_nota)

media_menos10 = media * 0.9
media_mais10 = media * 1.1

nota_med_menos10 = 0
nota_med_mais10 = 0

for i in range(N):
    if lista_nota[i] > media_mais10:
        nota_med_mais10 += 1

for i in range(N):
    if lista_nota[i] < media_menos10:
        nota_med_menos10 += 1

print('{:.2f}'.format(media))
print(nota_med_mais10)
print(nota_med_menos10)
