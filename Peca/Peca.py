import Peao, Torre, Cavalo, Bispo, Rainha, Rei
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
	def movimentosPossiveis(self,tabuleiro):
		pass

	@abstractmethod
	def tipo():
		pass
		
	

