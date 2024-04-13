# Pares, Ímpares, Positivos e Negativos.

N = int(input())

if N == 0:
  print('\nNULO')

elif N > 0:
  if N % 2 == 0:
    print('\nPOSITIVO PAR')

  else:
    print('\nPOSITIVO IMPAR')

else:
  if N % 2 == 0:
    print('\nNEGATIVO PAR')

  else:
    print('\nNEGATIVO IMPAR')

