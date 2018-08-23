import pytest

import Tabuleiro

def test_configuracao_inicial():
	t=Tabuleiro()
	#brancas
	assert t.pecaNaPosicao('a1').tipo() == 'torre'
	assert t.pecaNaPosicao('h1').tipo() == 'torre'
	assert t.pecaNaPosicao('b1').tipo() == 'cavalo'
	assert t.pecaNaPosicao('g1').tipo() == 'cavalo'
	assert t.pecaNaPosicao('c1').tipo() == 'bispo'
	assert t.pecaNaPosicao('f1').tipo() == 'bispo'
	assert t.pecaNaPosicao('d1').tipo() == 'rainha'
	assert t.pecaNaPosicao('e1').tipo() == 'rei'
	
	for i in ['a','b','c','d','e','f','g','h']:
		assert t.pecaNaPosicao(i + '2').tipo()=='peao'
	#pretas

	assert t.pecaNaPosicao('a8').tipo() == 'torre'
	assert t.pecaNaPosicao('h8').tipo() == 'torre'
	assert t.pecaNaPosicao('b8').tipo() == 'cavalo'
	assert t.pecaNaPosicao('g8').tipo() == 'cavalo'
	assert t.pecaNaPosicao('c8').tipo() == 'bispo'
	assert t.pecaNaPosicao('f8').tipo() == 'bispo'
	assert t.pecaNaPosicao('d8').tipo() == 'rainha'
	assert t.pecaNaPosicao('e8').tipo() == 'rei'

	for i in ['a','b','c','d','e','f','g','h']:
		assert t.pecaNaPosicao(i + '7').tipo() == 'peao'

def test_movimentacao_peao():
	
