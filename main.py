# Considera um sistema de apoio à gestão das visualizações de
# canais para uma smart TV.

# Pretendemos que desenvolvas uma aplicação em Python para a visualização
# semanal das estatísticas das visualizações dos canais disponíveis. Cada
# visualização é caracterizada pela sigla do canal (e.g., TVI) e pelo tempo de
# visualização num dia da semana (e.g., segunda-feira, 32 minutos). Na pasta de
# apoio ao projeto tens um ficheiro de texto com um exemplo dos dados guardados
# durante uma semana que deves considerar. Este ficheiro foi gerado
# aleatoriamente pelo programa que tens nesta pasta. Podes alterar os dados, mas
# deves manter o seu formato e o nome ficheiro.

# A aplicação deve disponibilizar as seguintes funcionalidades,
# através de um menu:

# F1 - Mostrar no ecrã as visualizações dos canais que estão guardadas no
#      ficheiro de texto.
# F2 - Pesquisar se determinado canal foi visto durante a semana, recorrendo a
#      um algoritmo de pesquisa sequencial.
# F3 - Mostrar a lista dos canais da smart TV, ordenada por ordem decrescente do
#      número de visualizações pelo algoritmo insertion sort.
# F4 - Mostrar as visualizações de um determinado canal da smart TV num
#      determinado dia da semana (pesquisa o canal pela sigla)

from gera_visualizacoes import main as gen
from f1 import somar_visualizacoes
from f2 import canal_visto
from f3 import sort_canais
from f4 import get_visualizacoes

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2, width=60)

def main():

  print("1: (F1) Mostrar as visualizações de todos os canais")
  print("2: (F2) Verificar se um canal foi visto durante a semana")
  print("3: (F3) Lista de canais")
  print("4: (F4) Mostrar as visualizações de um canal específico")
  print("5: ---- Gerar novos canais")

  vis = somar_visualizacoes("visualizacoes.txt")

  while True:
    _input = input("> ")
    if len(_input) == 1 and any(map(lambda i: str(i) == _input, [1,2,3,4,5])):
      if _input == "1":
        pp.pprint(vis)
      if _input == "2":
        _canal = input("> Canal: ")
        print(canal_visto(vis, _canal))
      if _input == "3":
        pp.pprint(sort_canais(vis))
      if _input == "4":
        _canal = input("> Canal: ")
        while True:
          _dia = input("> Dia da semana: ")
          if any(map(lambda i: str(i) == _dia, [1,2,3,4,5,6,7])):
            break
          print("1, 2, 3, 4, 5, 6, ou 7, por favor.")
        print(get_visualizacoes(vis, _canal, int(_dia)))
      if _input == "5":
        gen()
        print("Novos canais escritos em visualizacoes.txt")
      break
    print("1, 2, 3, ou 4, por favor.")

main()
