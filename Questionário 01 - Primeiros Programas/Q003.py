# Aumento de Salário

salario = float(input('\n'))
aumento = float(input())

Nsalario = salario + salario * aumento/100

print('Seu salario teve aumento de {} %, passando de R$ {} para R$ {}'.format(aumento, salario, Nsalario))
