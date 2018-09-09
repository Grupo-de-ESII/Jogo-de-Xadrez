from abc import ABC,abstractmethod

class Peca(ABC):
	self.jogador=0
	def __init__(self, nome,jogador):
		l={
			'peao' : Peao,
			'torre' : Torre,
			'cavalo' : Cavalo,
			'bispo' : Bispo,
			'rainha' : Rainha,
			'rei' : Rei}
		return l[nome](jogador)
	
	@abstractmethod
	def movimentosPossiveis(self,posicao,tabuleiro):
		pass

	@abstractmethod
	def tipo():
		pass

class Rei(Peca):
	self.jaMeMovi = False
	def __init__(self,posicao,jogador):
		self.jogador=jogador

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		inc=[(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
		for(i in inc):
			(incx,incy)=i
			if(x+incx>7 or x+incx<0 or y+incy>7 or y+incy<0):
				continue
			if (not tabuleiro.temPecaNaPosicao((x+incx,y+incy))):
        			l.append([['rei',posicao,(x+i,y+i)]])
      			elif (tabuleiro.playerPecaNaPosicao((x+incx,y+incy))!=jogador):
        			l.append([['peao',posicao,(x+incx,y+incy)]])
		return l
			
	
	
	def tipo(self):
		return 'rei'
			
class Bispo(Peca):
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
      elif (tabuleiro.playerPecaNaPosicao((x+i,y+i))!=jogador):
        l.append([['bispo',posicao,(x+i,y+i)]])
      else:
	break
	
    for i in [1,2,3,4,5,6,7]:
      #se movendo em direção ao canto inferior esquerdo na visão das brancas
      if (x-i)<0 or (y-i)<0:
        break;
      if (not tabuleiro.temPecaNaPosicao((x-i,y-i))):
        l.append([['bispo',posicao,(x-i,y-i)]])
      elif (tabuleiro.playerPecaNaPosicao((x-i,y-i))!=jogador):
        l.append([['bispo',posicao,(x-i,y-i)]])
      else:
	break
	
    for i in [1,2,3,4,5,6,7]:
      #se movendo em direção ao canto inferior direito na visão das brancas
      if (x+i)<0 or (y-i)<0:
        break;
      if (not tabuleiro.temPecaNaPosicao((x+i,y-i))):
        l.append([['bispo',posicao,(x+i,y-i)]])
      elif (tabuleiro.playerPecaNaPosicao((x+i,y-i))!=jogador):
        l.append([['bispo',posicao,(x+i,y-i)]])
      else:
	break

    for i in [1,2,3,4,5,6,7]:
      #se movendo em direção ao canto superior esquerdo na visão das brancas
      if (x-i)<0 or (y+i)<0:
        break;
      if (not tabuleiro.temPecaNaPosicao((x-i,y+i))):
        l.append([['bispo',posicao,(x-i,y+i)]])
      elif (tabuleiro.playerPecaNaPosicao((x-i,y+i))!=jogador):
        l.append([['bispo',posicao,(x-i,y+i)]])
      else:
	break
    
    return l
      
        
  
  def tipo(self):
    return 'bispo'

class Peao(Peca):
	self.primeiroMovimento = False
	def __init__(self,posicao,jogador):
		self.jogador=jogador

	def movimentosPossiveis(self,posicao,tabuleiro):
		l=[]
		(x,y)=posicao
		incrementoPlayer = 1 if player.cor == 'branca' else -1
		if(primeiromovimento):
			if not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer)) \
			and not tabuleiro.temPecaNaPosicao((x,y+2*incrementoPlayer)):
				l.append([['peao',posicao,(x,y+2*incrementoPlayer)]])
		#mover para frente
		if(not tabuleiro.temPecaNaPosicao((x,y+incrementoPlayer))):
			l.append([['peao',posicao,(x,y+incrementoPlayer)]])
		#captura para a direita
		if(tabuleiro.temPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer))\
		   and tabuleiro.playerPecaNaPosicao((x+incrementoPlayer,y+incrementoPlayer)) != player):
			l.append([['peao',posicao,(x+incrementoPlayer,y+incrementoPlayer)]])
			
		#captura para a esquerda
		if(tabuleiro.temPecaNaPosicao((x-incrementoPlayer,y-incrementoPlayer))\
		   and tabuleiro.playerPecaNaPosicao((x-incrementoPlayer,y-incrementoPlayer)) != player):
			l.append([['peao',posicao,(x-incrementoPlayer,y-incrementoPlayer)]])
		return l
			
	
	
	def tipo(self):
		return 'peao'
			

		
	

