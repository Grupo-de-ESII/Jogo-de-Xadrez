from Tabuleiro import *

tab=Tabuleiro()

#Possiveis movimentos dos dois jogadores são diferentes?
assert tab.jogadorPossiveisMovimentos(tab.pecas[0][0].jogador) != tab.jogadorPossiveisMovimentos(tab.pecas[0][7].jogador)

#Torre branca esta incapaz de mover-se

assert tab.pecas[0][0].tipo()=='torre'
assert tab.pecas[0][0].jogador.cor=='branca'
assert tab.pecaPossiveisMovimentos((0,0)) == []


