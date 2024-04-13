# Área

A, B, C = input('\n').split()
A = float(A)
B = float(B)
C = float(C)

a = (A * C) / 2
b = 3.14159 * C ** 2
c = (A + B) * C / 2
d = B ** 2
e = A * B

print('TRIANGULO: {:.3f}'.format(a))
print('CIRCULO: {:.3f}'.format(b))
print('TRAPEZIO: {:.3f}'.format(c))
print('QUADRADO: {:.3f}'.format(d))
print('RETANGULO: {:.3f}\n'.format(e))
