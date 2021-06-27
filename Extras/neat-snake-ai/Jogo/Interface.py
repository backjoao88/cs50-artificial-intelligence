
# Copyright (C) 2021 João Paulo Back

import pygame

class PygameInterface:
    def __init__(self, TamanhoTabela, Janela):
        self.TamanhoTabela  = TamanhoTabela
        self.Janela         = Janela

    def __contains__(self, Posicao):
        return 0 <= Posicao[0] < self.TamanhoTabela[0] and 0 <= Posicao[1] < self.TamanhoTabela[1]

    def DesenharBloco(self, Posicao, Cor):
        LarguraBloco = self.Janela.get_width() // self.TamanhoTabela[0]
        AlturaBloco = self.Janela.get_height() // self.TamanhoTabela[1]
        pygame.draw.rect(self.Janela, Cor, (Posicao[0] * LarguraBloco, Posicao[1] * AlturaBloco, LarguraBloco, AlturaBloco))
