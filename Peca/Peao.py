import typing

import Peca

class Peao(Peca):
	self.primeiroMovimento:bool = False
	def __init__(self,posicao,jogador):
		self.posicao=posicao
		self.jogador=jogador

	def movimentosPossiveis(self,tabuleiro):
		l=[]
		(x,y) = posicao
		if(primeiromovimento):
			if(tabuleiro[x][y+1] == None && tabuleiro[x][y+2] == None):
				l = l + []
			
