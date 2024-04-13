# Festa da Marilda 2

lista = []

while True:
    nomes = str(input())
    if nomes == "FIM":
        break
    lista.append(nomes)

for nome in sorted(lista):
    print(nome)

while True:
    N = int(input())
    if N == 0:
        break

    print('--------------------------------------------------')
    for _ in range(N):
        novos_nomes = str(input())
        lista.append(novos_nomes)

    for nome in sorted(lista):
        print(nome)

