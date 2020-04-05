from gera_visualizacoes import main as gen
from f1 import somar_visualizacoes
from random import choice as rchoice

def canal_visto(canais, sigla):
  # if (sigla in canais): return True

  # "sequencial"
  for c in canais.keys():
    if (c == sigla): return True
  return False

def main():
  gen() # novos canais
  vis = somar_visualizacoes("visualizacoes.txt")
  canal = rchoice(list(vis.keys())) # canal à sorte
  print(canal_visto(vis, canal))

# main()
