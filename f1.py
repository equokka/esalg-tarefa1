from pprint import PrettyPrinter

def somar_visualizacoes(fname):
  canais = {}
  with open(fname, "r") as f:
    lines = f.read().split("\n")
    lines.pop() # remove last line
    for line in lines:
      d = line.split(" ")

      # 0 - sigla
      # 1 - minutos de visualizacao
      # 2 - dia da semana
      sigla = d[0]
      mins  = int(d[1])
      dia   = int(d[2])

      # https://docs.python.org/3/library/stdtypes.html#dict.setdefault
      # https://stackoverflow.com/a/12906014/12086004
      # isto cria o canal se não existir já
      canais.setdefault(sigla, [])

      # adicionamos a visualizacao
      canais[ sigla ].append({ "dia": dia, "tempo": mins })
  return canais

def main():
  pp = PrettyPrinter(indent=2)
  pp.pprint(somar_visualizacoes("visualizacoes.txt"))

# main()
