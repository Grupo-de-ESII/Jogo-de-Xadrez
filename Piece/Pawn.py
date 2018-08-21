import typing

import Piece

class Pawn(Piece):
	firstMove:bool = False
	def __init__(self,position,player):
		self.position=position
		self.player=player

	def getPossibleMoves(self,board):
		l=[]
		if(firstMove):
			
