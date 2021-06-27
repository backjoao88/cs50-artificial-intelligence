import pygame
from Config.Constantes import Movimentos

class JogadorHumano:
  
  def __init__(self, Acao = Movimentos.BAIXO.value):
    self.Acao = Acao

  def Jogar(self, Jogo = None, Eventos = None):
    NovaAcao = self.Acao
    for Evento in Eventos:
      if Evento.type == pygame.KEYDOWN:
        if Evento.key == pygame.K_LEFT and self.Acao != Movimentos.DIREITA.value:
          NovaAcao = Movimentos.ESQUERDA.value
        elif Evento.key == pygame.K_RIGHT and self.Acao != Movimentos.ESQUERDA.value:
          NovaAcao = Movimentos.DIREITA.value
        elif Evento.key == pygame.K_UP and self.Acao != Movimentos.BAIXO.value:
          NovaAcao = Movimentos.CIMA.value
        elif Evento.key == pygame.K_DOWN and self.Acao != Movimentos.CIMA.value:
          NovaAcao =  Movimentos.BAIXO.value
    self.Acao = NovaAcao
    return NovaAcao