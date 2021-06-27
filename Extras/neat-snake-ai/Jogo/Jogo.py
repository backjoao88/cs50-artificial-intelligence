
# Copyright (C) 2021 João Paulo Back

import pygame

from Config.Constantes  import Cores, Movimentos, ConfiguracoesGerais
from Modelos.Comida     import Comida
from Modelos.Cobra      import Cobra
from Jogo.Interface     import PygameInterface

import os

pygame.mixer.init(buffer=512)

class Jogo:

    def __init__(self, TamanhoJanela, TabelaTamanho, PosicaoInicial, Jogador):
        self.Janela         = pygame.display.set_mode(TamanhoJanela)
        self.Tabela         = PygameInterface(TabelaTamanho, self.Janela)
        self.PosicaoInicial = PosicaoInicial

        self.CobraObj       = Cobra(self.PosicaoInicial, Movimentos.BAIXO.value)
        self.ComidaObj      = Comida.PosicaoAleatoria(self.Tabela)
        self.Tempo          = sum(self.Tabela.TamanhoTabela)
        self.TempoRestante  = 2 * self.Tempo
        self.Pontuacao      = 0
        self.Jogador        = Jogador

        pygame.display.set_caption("Jogo da Cobrinha AI")

    def Redesenhar(self, CobraObj, ComidaObj, Pontuacao, TempoRestante):
        self.Janela.fill(Cores.PRETO.value)
        self.CobraObj.Desenhar(self.Tabela)
        self.ComidaObj.Desenhar(self.Tabela)
        pygame.display.update()

    def Jogar(self):

        ClockFPS = pygame.time.Clock()
        fps = ConfiguracoesGerais.TAXA_FPS.value
        while True:

            ClockFPS.tick(fps)

            Eventos = pygame.event.get()

            for Evento in Eventos:
                if Evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if Evento.type == pygame.KEYDOWN:
                    if Evento.key == pygame.K_SPACE:
                        fps = 15

            self.CobraObj.Mover()

            self.TempoRestante -= 1
            if self.TempoRestante < 0:
                return self.Pontuacao

            self.Pontuacao += 0.005

            self.CobraObj.Direcao = self.Jogador.Jogar(Jogo = self, Eventos = Eventos)

            if self.CabecaCobra() not in self.Tabela or self.CabecaCobra() in self.CorpoCobra():
                return self.Pontuacao

            if self.CabecaCobra() == self.ComidaObj.Posicao:
                self.Pontuacao += 1
                self.CobraObj.Tamanho += 1
                self.ComidaObj = Comida.PosicaoAleatoria(self.Tabela)
                self.TempoRestante += self.Tempo

            self.Redesenhar(self.CobraObj, self.ComidaObj, self.Pontuacao, self.TempoRestante)

    def CabecaCobra(self):
        return self.CobraObj.Corpo[0]

    def CorpoCobra(self):
        return self.CobraObj.Corpo[1:]

    def EntradasRedeNeural(self):

        Cabeca = self.CabecaCobra()

        AutoColisaoEsquerda = 0
        for x in range(Cabeca[0]):
            if (x, Cabeca[1]) in self.CobraObj.Corpo:
                AutoColisaoEsquerda = x

        AutoColisaoDireita = self.Tabela.TamanhoTabela[0]
        for x in range(self.Tabela.TamanhoTabela[0], Cabeca[0], -1):
            if (x, Cabeca[1]) in self.CobraObj.Corpo:
                AutoColisaoDireita = x

        AutoColisaoCima = 0
        for y in range(Cabeca[1]):
            if (Cabeca[0], y) in self.CobraObj.Corpo:
                AutoColisaoCima = y

        AutoColisaoBaixo = self.Tabela.TamanhoTabela[1]
        for y in range(self.Tabela.TamanhoTabela[1], Cabeca[1], -1):
            if (Cabeca[0], y) in self.CobraObj.Corpo:
                AutoColisaoBaixo = y

        DistanciaAutoColisaoCima      = Cabeca[1] - AutoColisaoCima
        DistanciaAutoColisaoBaixo     = AutoColisaoBaixo - Cabeca[1]
        DistanciaAutoColisaoEsquerda  = Cabeca[0] - AutoColisaoEsquerda
        DistanciaAutoColisaoDireita   = AutoColisaoDireita - Cabeca[0]

        DirecaoX, DirecaoY = self.CobraObj.Direcao

        EntradaRedeNeural = (DistanciaAutoColisaoCima, DistanciaAutoColisaoBaixo, DistanciaAutoColisaoEsquerda, DistanciaAutoColisaoDireita, self.ComidaObj.Posicao[0] - Cabeca[0], self.ComidaObj.Posicao[1] - Cabeca[1], DirecaoX, DirecaoY)

        return EntradaRedeNeural