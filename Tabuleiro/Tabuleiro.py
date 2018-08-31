#This file declares the Board Class, that contain the Pieces
#and is a high-level interface to the user use the piece

from typing import *

import Peca




class Tabuleiro():
	Pecas: List[List[Peca]] = [[None for j in range(8)] for i in range(8)]
	def __init__(self,player1: Jogador, player2: Jogador):



		#pawn
		for i in range(8):
			Pecas[i][1] = Peca('pawn', player1)
			Pecas[i][0] = Peca(pieceFromIndex(i), player1)

		for i in range(8):
			pieces[i][6] = Peca('pawn', player2)
			pieces[i][7] = Peca(pieceFromIndex(i), player2)

	def possiveisMovimentos():
		l=[]
		for i in range(8):
			for j in range(8):
				if (Pecas[i][j] != None):
					l = l + Pecas[i][j].possiveisMovimentos()
		return l

	#private methods, don't call
	#thanks to python by don't have private methods

	def __indexFromColumn(self,i):
		return chr(i+ord('a'))

	def __pieceFromIndex(self,i):
		l: List[str]=['tower','knight','bishop','queen','king','bishop','knight','rook']
		return l[i]
