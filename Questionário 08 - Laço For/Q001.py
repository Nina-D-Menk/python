# Vogais Alienígenas

def contar_vogais(vogais, frases):
    contador = len(vogais)
    total_vogais = 0
    for i in frases:
        for r in range(contador):
            if i == vogais[r]:
                total_vogais += 1

    return total_vogais


num_vez = int(input())
for _vezes in range(num_vez):
    vogais = str(input()).lower()
    frases = str(input()).lower()
    print(contar_vogais(vogais, frases))
