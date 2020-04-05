from pprint import PrettyPrinter
from random import choice as rchoice
from gera_visualizacoes import main as gen
from f1 import somar_visualizacoes

def get_visualizacoes(data, canal, dia):
  # 1.
  # filter(lambda vis: vis["dia"] == dia, data[canal])
  #   Isto retorna a lista do canal só com as entradas no dia correto.
  # 2. map(lambda i: i["tempo"], (...))
  #   Isto passa do formato "{'dia': 1, 'tempo': 27}"
  #   para simplesmente o número 27.
  return list(
    map(lambda i: i["tempo"],
      filter(lambda vis: vis["dia"] == dia, data[canal])
    )
  )

def main():
  gen() # novos canais
  vis = somar_visualizacoes("visualizacoes.txt")
  canal = rchoice(list(vis.keys())) # canal à sorte
  dia = rchoice([1, 2, 3, 4, 5, 6, 7]) # dia da semana à sorte
  print(get_visualizacoes(vis, canal, dia))

# main()
