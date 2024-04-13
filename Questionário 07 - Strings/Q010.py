# Risada Digital

def risada_digital(n):
    vogais = ['a', 'e', 'i', 'o', 'u']
    risada = []

    if len(n) > 50:
        return 'INVALIDA'

    for j in range(len(n)):
        if n[j] in vogais:
            risada.append(n[j])

    risada_sem_consoantes = ''.join(risada)

    if risada_sem_consoantes == '':
        return 'INVALIDA'

    if risada_sem_consoantes == risada_sem_consoantes[::-1]:
        return True

    else:
        return False


N = int(input())

for _ in range(N):
    string = input().lower()

    if risada_digital(string) == 'INVALIDA':
        print("INVALIDA")

    if risada_digital(string):
        print("ENGRACADA")

    if not risada_digital(string):
        print("SEM GRACA")
