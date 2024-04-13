#Q Soma de Primos é um Primo?

def eprimo(primo):
    if primo <= 1:
        return False

    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False

    return True


def soma_primos(x, y):
    if eprimo(x) and eprimo(y):
        soma_de_valores = sum([x, y])
        if eprimo(soma_de_valores):
            return print("A soma de {} e {} eh um primo".format(valor_1, valor_2))

        else:
            return print("A soma de {} e {} nao eh um primo".format(valor_1, valor_2))


valor_1 = int(input())
valor_2 = int(input())

if not eprimo(valor_1):
    print("O numero {} nao eh primo".format(valor_1))

elif not eprimo(valor_2):
    print("O numero {} nao eh primo".format(valor_2))

else:
    soma_primos(valor_1, valor_2)
