from functools import *

class Rainha:
	def __init__(self,jogador):
		self.jogador=jogador
	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção a direita
			if (x+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y))):
				l.append([['rainha',posicao,(x+i,y)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y))!=self.jogador):
				l.append([['rainha',posicao,(x+i,y)]])
				break
			else:
				break
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção a esquerda
			if (x-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x-i,y))):
				l.append([['rainha',posicao,(x-i,y)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y))!=self.jogador):
				l.append([['rainha',posicao,(x-i,y)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo para baixo
			if (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x,y-i))):
				l.append([['rainha',posicao,(x,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x,y-i))!=self.jogador):
				l.append([['rainha',posicao,(x,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo para cima
			if (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x,y+i))):
				 l.append([['rainha',posicao,(x,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x,y+i))!=self.jogador):
				l.append([['rainha',posicao,(x,y+i)]])
				break
			else:
				break
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto superior direito na visão das brancas
			if (x+i)>7 or (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y+i))):
				l.append([['rainha',posicao,(x+i,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y+i))!=self.jogador):
				l.append([['rainha',posicao,(x+i,y+i)]])
				break
			else:
				break
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto inferior esquerdo na visão das brancas
			if (x-i)<0 or (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x-i,y-i))):
				l.append([['rainha',posicao,(x-i,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y-i))!=self.jogador):
				l.append([['rainha',posicao,(x-i,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto inferior direito na visão das brancas
			if (x+i)>7 or (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y-i))):
				l.append([['rainha',posicao,(x+i,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y-i))!=self.jogador):
				l.append([['rainha',posicao,(x+i,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto superior esquerdo na visão das brancas
			if (x-i)<0 or (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x-i,y+i))):
				 l.append([['rainha',posicao,(x-i,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y+i))!=self.jogador):
				l.append([['rainha',posicao,(x-i,y+i)]])
				break
			else:
				break
		return l 
	def tipo(self):
		return 'rainha'


class Torre:
	def __init__(self,jogador):
		self.jogador=jogador
	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção a direita
			if (x+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y))):
				l.append([['torre',posicao,(x+i,y)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y))!=self.jogador):
				l.append([['torre',posicao,(x+i,y)]])
				break
			else:
				break
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção a esquerda
			if (x-i)<0:
				break
			if (not tabuleiro.temPecaNaPosicao((x-i,y))):
				l.append([['torre',posicao,(x-i,y)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y))!=self.jogador):
				l.append([['torre',posicao,(x-i,y)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo para baixo
			if (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x,y-i))):
				l.append([['torre',posicao,(x,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x,y-i))!=self.jogador):
				l.append([['torre',posicao,(x,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo para cima
			if (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x,y+i))):
				 l.append([['torre',posicao,(x,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x,y+i))!=self.jogador):
				l.append([['torre',posicao,(x,y+i)]])
				break
			else:
				break
		return l

	def tipo(self):
		return 'torre'


class Cavalo:
	def __init__(self,jogador):
		self.jogador=jogador
	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		inc=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
		for i in inc:
			(incx,incy)=i
			if(x+incx>7 or x+incx<0 or y+incy>7 or y+incy<0):
				continue
			if (not tabuleiro.temPecaNaPosicao((x+incx,y+incy))):
        			l.append([['cavalo',posicao,(x+incx,y+incy)]])
			elif (tabuleiro.playerPecaNaPosicao((x+incx,y+incy))!=self.jogador):
        			l.append([['cavalo',posicao,(x+incx,y+incy)]])
		return l
	def tipo(self):
		return 'cavalo'



class Rei:
	def __init__(self,jogador):
		self.jaMeMovi=False
		self.jogador=jogador

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		inc=[(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
		for i in inc:
			(incx,incy)=i
			if(x+incx>7 or x+incx<0 or y+incy>7 or y+incy<0):
				continue
			if (not tabuleiro.temPecaNaPosicao((x+incx,y+incy))):
        			l.append([['rei',posicao,(x+incx,y+incy)]])
			elif (tabuleiro.playerPecaNaPosicao((x+incx,y+incy))!=self.jogador):
        			l.append([['rei',posicao,(x+incx,y+incy)]])
		return l


	def estouEmXeque(self,posicao,tabuleiro):
		for i in range(8):
			for j in range(8):
				if(tabuleiro.pecas[i][j] is not None and tabuleiro.pecas[i][j].jogador!=self.jogador):
					movimentosPecaInimiga=tabuleiro.pecas[i][j].movimentosPossiveis((i,j),tabuleiro)
					posicoesFinais=[p for p in map(lambda x: x[0][2],movimentosPecaInimiga)]
					if(posicoesFinais.count(posicao) != 0):
						return True
		return False
	def tipo(self):
		return 'rei'

class Bispo:
	def __init__(self,jogador):
		self.jogador=jogador

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto superior direito na visão das brancas
			if (x+i)>7 or (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y+i))):
				l.append([['bispo',posicao,(x+i,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y+i))!=self.jogador):
				l.append([['bispo',posicao,(x+i,y+i)]])
				break
			else:
				break
		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto inferior esquerdo na visão das brancas
			if (x-i)<0 or (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x-i,y-i))):
				l.append([['bispo',posicao,(x-i,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y-i))!=self.jogador):
				l.append([['bispo',posicao,(x-i,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto inferior direito na visão das brancas
			if (x+i)>7 or (y-i)<0:
				break;
			if (not tabuleiro.temPecaNaPosicao((x+i,y-i))):
				l.append([['bispo',posicao,(x+i,y-i)]])
			elif (tabuleiro.playerPecaNaPosicao((x+i,y-i))!=self.jogador):
				l.append([['bispo',posicao,(x+i,y-i)]])
				break
			else:
				break

		for i in [1,2,3,4,5,6,7]:
			#se movendo em direção ao canto superior esquerdo na visão das brancas
			if (x-i)<0 or (y+i)>7:
				break;
			if (not tabuleiro.temPecaNaPosicao((x-i,y+i))):
				 l.append([['bispo',posicao,(x-i,y+i)]])
			elif (tabuleiro.playerPecaNaPosicao((x-i,y+i))!=self.jogador):
				l.append([['bispo',posicao,(x-i,y+i)]])
				break
			else:
				break
		return l



	def tipo(self):
		return 'bispo'

class Peao:
	def __init__(self,jogador):
		self.jogador=jogador
		self.primeiroMovimento=True

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		incrementoPlayer = 1 if self.jogador.cor == 'branca' else -1
		if(self.primeiroMovimento):
			if not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer)) \
			and not tabuleiro.temPecaNaPosicao((x,y+2*incrementoPlayer)):
				l.append([['peao',posicao,(x,y+2*incrementoPlayer)]])
		#mover para frente
		if( 0<=y+incrementoPlayer<=7 and not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer))):
			l.append([['peao',posicao,(x,y+incrementoPlayer)]])
		#captura para a direita
		if(0<=x+incrementoPlayer<=7 and 0<=y+incrementoPlayer<=7 \
		and tabuleiro.temPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer))\
		   and tabuleiro.playerPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer)) != self.jogador):
			l.append([['peao',posicao,(x+incrementoPlayer,y+incrementoPlayer)]])

		#captura para a esquerda
		if(0<=x-incrementoPlayer<=7 and 0<=y+incrementoPlayer<=7
		   and tabuleiro.temPecaNaPosicao((x-incrementoPlayer,y+incrementoPlayer))\
		   and tabuleiro.playerPecaNaPosicao((x-incrementoPlayer,y+incrementoPlayer)) != self.jogador):
			l.append([['peao',posicao,(x-incrementoPlayer,y+incrementoPlayer)]])
		return l



	def tipo(self):
		return 'peao'





