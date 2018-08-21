import Pawn, Rook, Knight, Bishop, Queen,King
from abc import ABC,abstractmethod

class Piece(ABC):
	self.position=0
	self.player=0
	def __init__(self, name,position,player):
		l={
			'pawn' : Pawn,
			'rook' : Rook,
			'knight' : Knight,
			'bishop' : Bishop,
			'queen' : Queen,
			'king' : King}
		return l[name](position,player)
	
	@abstractmethod
	def getPossibleMoves(self,board):
		pass

	@abstractmethod
	def move(self,position):
		pass
	

