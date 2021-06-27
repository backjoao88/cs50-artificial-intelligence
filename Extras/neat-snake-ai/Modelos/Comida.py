
# Copyright (C) 2021 João Paulo Back

from random             import randrange
from Config.Constantes  import Cores, Movimentos

class Comida:

    def __init__(self, Posicao):
      self.Posicao = Posicao

    @staticmethod
    def PosicaoAleatoria(Tabela):
      return Comida((randrange(0, Tabela.TamanhoTabela[0]), randrange(0, Tabela.TamanhoTabela[1])))

    def Desenhar(self, Tabela):
      Tabela.DesenharBloco(self.Posicao, Cores.VERMELHO.value)

