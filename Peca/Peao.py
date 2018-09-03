import typing

import Peca

class Peao(Peca):
	self.primeiroMovimento:bool = False
	def __init__(self,posicao,jogador):
		self.jogador=jogador

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		incrementoPlayer = 1 if player.cor == 'branca' else -1
		if(primeiromovimento):
			if not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer))
			and not tabuleiro.temPecaNaPosicao((x,y+2*incrementoPlayer)):
				l.append([['peao',posicao,(x,y+2*incrementoPlayer)]])
		#mover para frente
		if(not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer))):
			l.append([['peao',posicao,(x,y+incrementoPlayer)]])
		#captura para a direita
		if(tabuleiro.temPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer))
		   and tabuleiro.playerPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer)) != player):
			l.append([['peao',posicao,(x+incrementoPlayer,y+incrementoPlayer)]])
			
		#captura para a esquerda
		if(tabuleiro.temPecaNaPosicao((x-incrementoPlayer,y-incrementoPlayer))
		   and tabuleiro.playerPecaNaPosicao((x-incrementoPlayer,y-incrementoPlayer)) != player):
			l.append([['peao',posicao,(x-incrementoPlayer,y-incrementoPlayer)]])
		return l
			
	
	
	def tipo(self):
		return 'peao'
			
