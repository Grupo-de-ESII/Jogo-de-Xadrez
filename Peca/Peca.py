import Peao, Torre, Cavalo, Bispo, Rainha, Rei
from abc import ABC,abstractmethod

class Peca(ABC):
	self.posicao=0
	self.jogador=0
	def __init__(self, nome,posicao,jogador):
		l={
			'peao' : peao,
			'torre' : Torre,
			'cavalo' : Cavalo,
			'bispo' : Bispo,
			'rainha' : Rainha,
			'rei' : Rei}
		return l[nome](posicao,jogador)
	
	@abstractmethod
	def movimentosPossiveis(self,tabuleiro):
		pass

	@abstractmethod
	def mover(self,posicao):
		pass
	

