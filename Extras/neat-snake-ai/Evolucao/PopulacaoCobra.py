import neat
import pickle
from Jogo.Jogo import Jogo
from Evolucao.JogadorArtificial import JogadorArtificial

class NeatPopulacaoCobra:

  def __init__(self, CaminhoConfig = None, Populacao = None):
    self.Config        = self.ConfiguracaoNeat(CaminhoConfig)
    self.NeatPopulacao = Populacao if Populacao is not None else self.NovaPopulacao()
    self.MelhorGenoma = None
    self.AdicionarReportagem(neat.StdOutReporter(True))
    self.AdicionarReportagem(self.EstatisticasAtuais())

  def EstatisticasAtuais(self):
    return neat.StatisticsReporter()

  def ConfiguracaoNeat(self, CaminhoConfig):
    return neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, CaminhoConfig)

  def SalvarPopulacao(self):
    with open('Populacao.dat', 'wb') as Arquivo:
        pickle.dump(self.NeatPopulacao, Arquivo, pickle.HIGHEST_PROTOCOL)

  def SalvarMelhorGenoma(self):
    with open('Genoma.pkl', 'wb') as Arquivo:
        pickle.dump(self.MelhorGenoma, Arquivo, pickle.HIGHEST_PROTOCOL)

  def CarregarPopulacao(NomeArquivo):
    with open(NomeArquivo, 'rb') as Arquivo:
      return pickle.load(Arquivo)

  def NovaPopulacao(self):
    return neat.Population(self.Config)
  
  def AdicionarReportagem(self, Reportagem):
    self.NeatPopulacao.add_reporter(Reportagem)
  
  def RemoverReportagem(self, Reportagem):
    self.NeatPopulacao.remove(Reportagem)

  def Evoluir(self, Geracoes = 1):
    self.MelhorGenoma = self.NeatPopulacao.run(self.Jogar, Geracoes)
    self.SalvarMelhorGenoma()
    
  def Jogar(self, Genomas, Config):
    for _, Genoma in Genomas:
      RedeNeural = neat.nn.FeedForwardNetwork.create(Genoma, Config)
      if not Genoma.fitness:
        Genoma.fitness = 0
      JogadorIA = Jogo((800, 600), (40, 30), (5, 5), JogadorArtificial(RedeNeural))
      Genoma.fitness += JogadorIA.Jogar()
