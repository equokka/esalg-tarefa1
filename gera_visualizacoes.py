from random import randint

def gerar_sigla(chars):
  return "".join(
    [str(chars[randint(0, len(chars) - 1)]) for c in range(3)]
  )

def gerar_fich_visualizacoes(num_visualizacoes, fname):
  with open(fname, "w") as f:
    for _ in range(num_visualizacoes):
      f.write(
        str( gerar_sigla(["a", "b", "1"]) ) + " " +
        str( randint(1, 45)               ) + " " +
        str( randint(1, 7)                ) + "\n"
      )

# eg. 11b    38    3
#     sigla  |     dia da semana
#            num visualizações

def main():
  gerar_fich_visualizacoes(100, "visualizacoes.txt")

# main()
