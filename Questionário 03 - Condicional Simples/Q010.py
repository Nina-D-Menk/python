# Médias

media = input('\n')
a = int(input())
b = int(input())
c = int(input())

def medias(media, a, b, c):
  if media == 'A':
    A = (a + b + c) / 3
    print('{:.3f}'.format(A))

  elif media == 'H':
    H = 3 / ((1 / a) + (1 / b) + (1 / c) )
    print('{:.3f}'.format(H))

  elif media == 'G':
    G = (a * b * c) ** (1 / 3)
    print('{:.3f}'.format(G))

medias(media, a, b, c)
