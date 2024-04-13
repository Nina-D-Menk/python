# Meses do Ano por extenso

def meses(a):

  if 1 <= a <= 12:
    mes = [
          "janeiro", "fevereiro", "marco", "abril",
          "maio", "junho", "julho", "agosto",
          "setembro", "outubro", "novembro", "dezembro"
          ]
    nome = mes[a - 1]
    return nome

  else:
    return "invalido"

mes_do_ano = int(input())
resultado = meses(mes_do_ano)
print(resultado)
