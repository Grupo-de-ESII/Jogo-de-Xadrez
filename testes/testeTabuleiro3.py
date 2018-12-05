from sys import *
path.append("../src/")

from Tabuleiro import *

tab=Tabuleiro()

#Possiveis movimentos dos dois jogadores são diferentes?
assert tab.jogadorPossiveisMovimentos(tab.pecas[0][0].jogador) != tab.jogadorPossiveisMovimentos(tab.pecas[0][7].jogador)

#Torre branca esta incapaz de mover-se

assert tab.pecas[0][0].tipo()=='torre'
assert tab.pecas[0][0].jogador.cor=='branca'
assert tab.pecaPossiveisMovimentos((0,0)) == []

aux={}
for i in tab.posicaoReis.keys():
	aux[i]=tab.posicaoReis[i]

tab.falsoMovimento((0,1),(0,3))

aux2={}
for i in tab.posicaoReis.keys():
	aux2[i]=tab.posicaoReis[i]


tab.falsoMovimento((0,3),(0,4))
tab.reset()
assert aux2 == tab.posicaoReis
tab.reset()

assert aux == tab.posicaoReis
