# Pesquisa de intenção de voto

def vantagem(p1, p2, n):
    maior_vantagem = 0.00

    for i in range(n):
        diferenca = p1[i] - p2[i]
        if diferenca > maior_vantagem:
            maior_vantagem = diferenca

    return maior_vantagem


N = int(input())
p1 = input().split()
p2 = input().split()
pesquisa1 = []
pesquisa2 = []

for i in range(N):
    pesquisa1.append(float(p1[i]))

for j in range(N):
    pesquisa2.append(float(p2[j]))

print('{:.2f}'.format(vantagem(pesquisa1, pesquisa2, N)))
