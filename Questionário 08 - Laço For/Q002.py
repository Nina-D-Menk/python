# Múltiplos de Cinco

num1, num2 = input().split()

num1, num2 = int(num1), int(num2)

for i in range(num1, num2 - 4):
    if i % 5 == 0:
        print(i, end='|')

for i in range(num2 - 4, num2 + 1):
    if i % 5 == 0:
        print(i)
