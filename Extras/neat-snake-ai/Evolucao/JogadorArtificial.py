from Config.Constantes import Movimentos

class JogadorArtificial:
  
  def __init__(self, Cerebro):
    self.Cerebro = Cerebro

  def Jogar(self, Jogo = None, Eventos = None):
    SaidaRedeNeural = self.Cerebro.activate(Jogo.EntradasRedeNeural())
    Direcoes = [
      [Movimentos.BAIXO.value, Movimentos.ESQUERDA.value],
      [Movimentos.DIREITA.value, Movimentos.CIMA.value],
    ]
    return Direcoes[SaidaRedeNeural[0] > 0.5][SaidaRedeNeural[1] > 0.5]
