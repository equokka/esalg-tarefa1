from gera_visualizacoes import main as gen
from f1 import somar_visualizacoes
from random import choice as rchoice

def canal_visto(canais, sigla):
  for k in canais[sigla].keys():
    if (canais[sigla][k] > 0): return True
  return False

gen() # novos canais
vis = somar_visualizacoes("visualizacoes.txt")
canal = rchoice(list(vis.keys())) # canal à sorte

print(canal_visto(vis, canal))
