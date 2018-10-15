import sys
import random

def get_melhor_jogada(tabuleiro, jogador1):
	jogadas = get_jogadas(tabuleiro, jogador1)

	melhor_valor = -sys.maxsize - 1  # Menor inteiro
	melhor_jogada = None

	for jogada in jogadas:
		valor_jogada = minimax(tabuleiro, 3, jogador1)

		if valor_jogada > melhor_jogada:
			melhor_valor = valor_jogada
			melhor_jogada = jogada

	return melhor_jogada

def get_jogadas(tabuleiro, jogador1):
	return [[[1, 0], [-1, 0]],
			[[0, 1], [0, -1]]]

def minimax(tabuleiro, profundidade, maximizando_player1):
	# Limite da profundidade atingido
	if profundidade == 0:  # TODO: Ou jogada é final
		return avalia_tabuleiro(tabuleiro, maximizando_player1)

	jogadas = get_jogadas()
	if maximizando_player1:
		melhor_valor = -sys.maxsize - 1  # Menor inteiro
		
		for jogada in jogadas:
			tabuleiro = joga_jogada(tabuleiro, jogada)
			melhor_jogada = max(melhor_jogada, minimax(tabuleiro, profundidade - 1, !maximizando_player1))
	else:
		melhor_valor = sys.maxsize  # Maior inteiro

		for jogada in jogadas:
			tabuleiro = joga_jogada(tabuleiro, jogada)
			melhor_jogada = min(melhor_jogada, minimax(tabuleiro, profundidade - 1, !maximizando_player1))

	return melhor_jogada

def avalia_tabuleiro(tabuleiro, maximizando_player1):
	valor_heuristica = heuristica(tabuleiro)
	if maximizando_player1:
		return valor_heuristica
	else:
		return -valor_heuristica

def heuristica(tabuleiro):
	return random.random() * 10

def joga_jogada(tabuleiro, jogada):
	return tabuleiro
