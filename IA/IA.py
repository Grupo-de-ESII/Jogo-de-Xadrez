import sys
import random
from Jogador.Jogador import *

from Tabuleiro.Tabuleiro import *

JOGADA_PECA = 0
JOGADA_DE = 1
JOGADA_PARA = 2


class IA:

	def __init__(self):
		# Inicializa tabuleiro
		self.tabuleiro = Tabuleiro()

		self.jogador_1 = Jogador('branca')
		self.jogador_2 = Jogador('preta')

		# Pesos das peças pra usar na heurística
		self.pesos = {'peao': 1, 'cavalo': 3, 'bispo': 3, 'torre': 5, 'rainha': 9, 'rei': 90, '': 0}

	def get_melhor_jogada(self, jogador1):
		jogadas = self.get_jogadas_possiveis()

		melhor_valor = -sys.maxsize - 1  # Menor inteiro
		melhor_jogada = None

		for jogada in jogadas:
			valor_jogada = self.minimax(3, jogador1)

			if valor_jogada > melhor_valor:
				melhor_valor = valor_jogada
				melhor_jogada = jogada

		return melhor_jogada

	def get_jogadas_possiveis(self):
		return self.tabuleiro.possiveisMovimentos()

	def minimax(self, profundidade, maximizando_player1):
		# Limite da profundidade atingido
		if profundidade == 0:  # TODO: Ou jogada é final
			return self.avalia_tabuleiro(maximizando_player1)

		jogadas = self.get_jogadas_possiveis()
		if maximizando_player1:
			melhor_valor = -sys.maxsize - 1  # Menor inteiro

			for jogada in jogadas:
				self.joga_jogada(jogada)
				melhor_valor = max(melhor_valor, self.minimax(profundidade - 1, not maximizando_player1))
				self.desfaz_jogada(jogada)

		else:
			melhor_valor = sys.maxsize  # Maior inteiro

			for jogada in jogadas:
				self.joga_jogada(jogada)
				melhor_valor = min(melhor_valor, self.minimax(profundidade - 1, not maximizando_player1))
				self.desfaz_jogada(jogada)

		return melhor_valor

	def avalia_tabuleiro(self, maximizando_player1):
		valor_heuristica = self.heuristica_simples()
		
		if maximizando_player1:
			return valor_heuristica
		else:
			return -valor_heuristica

	def heuristica_simples(self):
		somatorio = 0
		for i in range(8):
			for j in range(8):
				peca = self.tabuleiro.pecas[i][j]

				if peca is not None:
					tipo = peca.tipo()

					if peca.jogador == self.jogador_1:
						somatorio += self.pesos[tipo]
					else:
						somatorio -= self.pesos[tipo]
		return somatorio

	def joga_jogada(self, jogada):
		self.tabuleiro.falsoMovimento(jogada[0][JOGADA_DE], jogada[0][JOGADA_PARA])

	def desfaz_jogada(self, jogada):
		self.tabuleiro.reset()
