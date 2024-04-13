# Conta de luz

quantidade  = float(input('\n'))

residencia = quantidade * 1.50
desconto = residencia - residencia * 0.15

print('\nValor a ser pago: R$ {:.2f} reais'.format(residencia))
print('Valor a ser pago com desconto: R$ {:.2f} reais'.format(desconto))
