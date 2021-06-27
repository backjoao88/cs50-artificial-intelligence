from enum import Enum

class ConfiguracoesEvolucao(Enum):
  NUM_GERACOES = 10000

class ConfiguracoesGerais(Enum):
  TAXA_FPS               = 1000
  TAMANHO_TELA           = (800, 600)
  TAMANHO_TABELA         = (40, 30)
  POSICAO_INICIAL_COBRA  = (5, 5)

class Cores(Enum):
  PRETO       = (0, 0, 0)
  BRANCO      = (255, 255, 255)
  VERMELHO    = (255, 0, 0)
  CINZA_FRACO = (28, 28, 28)
  CINZA_FORTE = (79, 79, 79)

class Movimentos(Enum):
  CIMA      = (0, -1)
  BAIXO     = (0, 1)
  ESQUERDA  = (-1, 0)
  DIREITA   = (1, 0)
