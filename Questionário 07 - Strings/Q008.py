# Q8 Código entre amigas

def codigo(code):
  lista_cod = [
              ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
              ]
  lista = []

  for i in range(len(code)):
    lista.append(lista_cod[int(code[i])])

  print(lista)
  frase_codificada = ''.join(lista)
  return frase_codificada

while True:
  code = input().split()
  if code == ['6', '9','13']:
      break
  print(codigo(code))

