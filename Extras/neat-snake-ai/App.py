from Jogo.Interface               import PygameInterface
from Jogo.Jogo                    import Jogo
from Jogo.JogadorHumano           import JogadorHumano
from Evolucao.JogadorArtificial   import JogadorArtificial
from Modelos.Cobra                import Cobra
from Modelos.Comida               import Comida
from Evolucao.PopulacaoCobra      import NeatPopulacaoCobra
from Config.Constantes            import Cores, Movimentos, ConfiguracoesGerais, ConfiguracoesEvolucao

import os
import sys
import pickle
import neat

def Executar(CaminhoConfig, Populacao = None):
    Populacao   = Populacao if Populacao is not None else NeatPopulacaoCobra(CaminhoConfig)
    Populacao.Evoluir(ConfiguracoesEvolucao.NUM_GERACOES.value)
    Populacao.SalvarPopulacao()

if int(sys.argv[1]) == 1:
    ManipulacaoJogo = Jogo(ConfiguracoesGerais.TAMANHO_TELA.value, ConfiguracoesGerais.TAMANHO_TABELA.value, ConfiguracoesGerais.POSICAO_INICIAL_COBRA.value, JogadorHumano())
    ManipulacaoJogo.Jogar()
elif int(sys.argv[1]) == 2:
    CaminhoConfiguracao = os.path.join(os.path.dirname(__file__), 'Config.txt')
    Executar(CaminhoConfiguracao)
elif int(sys.argv[1]) == 3:
    CaminhoConfiguracao = os.path.join(os.path.dirname(__file__), 'Config.txt')
    with open("Genoma.pkl", 'rb') as Arquivo:
      Genoma = pickle.load(Arquivo)
    RedeNeural = neat.nn.FeedForwardNetwork.create(Genoma, neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, CaminhoConfiguracao))
    Jogador = Jogo((800, 600), (40, 30), (5, 5), JogadorArtificial(RedeNeural))
    Jogador.Jogar()