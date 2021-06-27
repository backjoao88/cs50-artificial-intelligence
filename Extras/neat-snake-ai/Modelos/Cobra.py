
# Copyright (C) 2021 João Paulo Back

from Config.Constantes  import Cores, Movimentos

class Cobra:
    
    def __init__(self, Posicao, Direcao):
      self.Corpo      = [Posicao]
      self.Direcao    = Direcao
      self.Tamanho     = 2

    def Desenhar(self, Tabela):
      Tabela.DesenharBloco(self.Corpo[0], Cores.CINZA_FORTE.value)
      for Index, Posicao in enumerate(self.Corpo[1:]):
        Tabela.DesenharBloco(Posicao, Cores.CINZA_FRACO.value if Index % 2 == 0 else Cores.CINZA_FRACO.value)

    def Mover(self):
      UltimaPosicaoCabeca = self.Corpo[0]
      NovaPosicaoCabeca   = (UltimaPosicaoCabeca[0] + self.Direcao[0], UltimaPosicaoCabeca[1] + self.Direcao[1])

      if self.Tamanho > 0:
        self.Corpo = [NovaPosicaoCabeca] + self.Corpo
        self.Tamanho -= 1
      else:
        self.Corpo = [NovaPosicaoCabeca] + self.Corpo[:-1]

