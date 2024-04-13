# Conta de Água e Esgoto

q, c = input('\n').split()
q = float(q)
c = float(c)

a = q * 1000 * c
b = a * 0.8
c = a + b

print('{:.2f}'.format(a))
print('{:.2f}'.format(b))
print('{:.2f}'.format(c))
