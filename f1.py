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
      canais.setdefault(sigla, {
        1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
      })

      # adicionamos os minutos de visualização ao dia da semana correto
      canais[ sigla ][ dia ] += mins
  return canais

pp = PrettyPrinter(indent=2)
pp.pprint(somar_visualizacoes("visualizacoes.txt"))
