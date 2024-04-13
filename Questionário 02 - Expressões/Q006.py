# Cédulas

N = int(input('\n'))

n1 = N // 100
a1 = N % 100
n2 = a1 // 50
a2 = a1 % 50
n3 = a2 // 20
a3 = a2 % 20
n4 = a3 // 10
a4 = a3 % 10
n5 = a4 // 5
a5 = a4 % 5
n6 = a5 // 2
a6 = a5 % 2
n7 = a6 // 1

print(N)
print('{} nota(s) de R$ 100,00'.format(n1))
print('{} nota(s) de R$ 50,00'.format(n2))
print('{} nota(s) de R$ 20,00'.format(n3))
print('{} nota(s) de R$ 10,00'.format(n4))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n6))
print('{} nota(s) de R$ 1,00\n'.format(n7))
