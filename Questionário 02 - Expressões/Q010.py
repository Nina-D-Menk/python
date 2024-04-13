# Conversão de tempo

n = int(input('\n'))

m = n // 60
s = n % 60
h = m // 60
m = m % 60

print('{}:{}:{}\n'.format(h, m, s))
