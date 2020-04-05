# F3 - Mostrar a lista dos canais da smart TV, ordenada por ordem decrescente do
#      número de visualizações pelo algoritmo insertion sort.

from gera_visualizacoes import main as gen
from f1 import somar_visualizacoes
from pprint import PrettyPrinter

def main():
  gen() # novos canais
  vis = somar_visualizacoes("visualizacoes.txt")

  # mete tudo numa lista em vez dum dicionario, para podermos ordenar
  ls = [{ "sigla": k, "vis": vis[k] } for k in vis.keys()]

  # insertion sort decrescente
  for index in range(1, len(ls)):
    move = index - 1
    while len(ls[index]["vis"]) > len(ls[move]["vis"]) and move >= 0:
      ls[move + 1] = ls[move]
      move -= 1
    ls[move + 1] = ls[index]

  pp = PrettyPrinter(indent=2)
  print("-" * 100)
  pp.pprint(ls)

main()
