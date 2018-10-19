#This file declares the Board Class, that contain the Pieces
#and is a high-level interface to the user use the piece


from Peca.Peca import *

class Tabuleiro:
	def __init__(self, player1, player2):
		self.pecas = [[None for j in range(8)] for i in range(8)]

		for i in range(8):
			self.pecas[i][1] = Peao(player1)
		self.pecas[0][0] = Torre(player1)
		self.pecas[1][0] = Cavalo(player1)
		self.pecas[2][0] = Bispo(player1)
		self.pecas[3][0] = Rei(player1)
		self.pecas[4][0] = Rainha(player1)
		self.pecas[5][0] = Bispo(player1)
		self.pecas[6][0] = Cavalo(player1)
		self.pecas[7][0] = Torre(player1)

		for i in range(8):
			self.pecas[i][6] = Peao(player2)
		self.pecas[0][7] = Torre(player2)
		self.pecas[1][7] = Cavalo(player2)
		self.pecas[2][7] = Bispo(player2)
		self.pecas[3][7] = Rei(player2)
		self.pecas[4][7] = Rainha(player2)
		self.pecas[5][7] = Bispo(player2)
		self.pecas[6][7] = Cavalo(player2)
		self.pecas[7][7] = Torre(player2)


	def possiveisMovimentos(self):
		l=[]
		for i in range(8):
			for j in range(8):
				if self.pecas[i][j] is not None:
					l = l + self.pecas[i][j].possiveisMovimentos()
		return l
	def tipoPecaNaPosicao(self, posicao):
		(x,y) = posicao
		if self.pecas[x][y] is not None:
			return self.pecas[x][y].tipo()
		return ''
	
	def temPecaNaPosicao(self, posicao):
		(x,y) = posicao
		return 0 <= x <= 7 and 0 <= y <= 7 and self.pecas[x][y] is not None


	def avalia(self, heuristica):
		return heuristica(self.pecas)
	#private methods, don't call
	#thanks to python by don't have private methods


	def indexFromColumn(self,i):
		return chr(i + ord('A'))


	def pieceFromIndex(self,i):
		l=['torre','cavalo','bispo','rainha','rei','bisto','cavalo','rook']
		return l[i]

	def matrix2str(self,posicao):
		(x,y)=posicao
		return self.indexFromColumn(x) + str(y+1)

	def str2matrix(self, str):
		return (ord(str[0])-ord('A'),int(str[1])-1)
