# Conta de energia de Rafinha

energia = int(input('\n'))

if energia <= 99:
  KWh = 1.35
  conta = energia * KWh

  if conta < 35:
    conta = 35
    print('{:.2f}'.format(conta))
    print(KWh)

  else:
    print('{:.2f}'.format(conta))
    print('{:.2f}'.format(KWh))

elif energia >= 100 and energia <= 299:
  KWh = 1.55
  conta = energia * KWh
  print('{:.2f}'.format(conta))
  print('{:.2f}'.format(KWh))

elif energia >= 300 and energia <= 574:
  KWh = 1.75
  conta = energia * KWh + (energia * KWh) * 0.10
  print('{:.2f}'.format(conta))
  print('{:.2f}'.format(KWh))

else:
  KWh = 2.15
  conta = energia * KWh + (energia * KWh) * 0.10
  print('{:.2f}'.format(conta))
  print('{:.2f}'.format(KWh))
