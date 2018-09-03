#This file declares the Board Class, that contain the Pieces
#and is a high-level interface to the user use the piece

from typing import *

import Peca




class Tabuleiro():
	pecas: List[List[Peca]] = [[None for j in range(8)] for i in range(8)]
	def __init__(self,player1: Jogador, player2: Jogador):



		#pawn
		for i in range(8):
			pecas[i][1] = Peca('pawn', player1)
			pecas[i][0] = Peca(pieceFromIndex(i), player1)

		for i in range(8):
			pecas[i][6] = Peca('pawn', player2)
			pecas[i][7] = Peca(pieceFromIndex(i), player2)

	def possiveisMovimentos(self):
		l=[]
		for i in range(8):
			for j in range(8):
				if (pecas[i][j] != None):
					l = l + Pecas[i][j].possiveisMovimentos()
		return l
	def tipoPecaNaPosicao(self,posicao):
		(x,y)=posicao
		if pecas[x][y] != None:
			return pecas[x][y].tipo()
		return ''
	
	def temPecaNaPosicao(self,posicao):
		(x,y)=posicao
		return x>=0 and x<= 7 and y>=0 and y<=7 and pecas[x][y]!=None
	#private methods, don't call
	#thanks to python by don't have private methods

	def __indexFromColumn(self,i):
		return chr(i+ord('a'))

	def __pieceFromIndex(self,i):
		l: List[str]=['tower','knight','bishop','queen','king','bishop','knight','rook']
		return l[i]
