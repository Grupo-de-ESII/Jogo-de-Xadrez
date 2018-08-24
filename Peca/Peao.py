import typing

import Peca

class Peao(Peca):
	self.primeiroMovimento:bool = False
	def __init__(self,posicao,jogador):
		self.posicao=posicao
		self.jogador=jogador

	def movimentosPossiveis(self,tabuleiro):
		l=[]
		if(primeiromovimento):
			minhaPosicao = Posicao(posicao)
			umaLinhaAcima=minhaPosicao.umaLinhaAcima()
			if(tabuleiro.pecaNaPosicao(umaLinhaAcima) == None && tabuleiro.pecaNaPosicao(umaLinhaAcima.umaLinhaAcima()) == None):
				l = l + [Jogada(self,)]
			
