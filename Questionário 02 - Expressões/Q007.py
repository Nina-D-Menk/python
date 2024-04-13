# Volume e área de um cilindro

altura = float(input('\n'))
raio = float(input())

v = 3.14 * altura * raio ** 2
a = 2 * 3.14 * raio * altura + 2 * 3.14 * raio ** 2

print('\n{:.2f}'.format(v))
print('{:.2f}\n'.format(a))
