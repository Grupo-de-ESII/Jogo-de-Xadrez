from sys import *
path.append("../src/")

from Tabuleiro import *

tab=Tabuleiro()

tab.falsoMovimento((0,1),(0,3))
tab.falsoMovimento((0,3),(0,4))
tab.reset()
tab.reset()

assert tab.xequeMate(1 if tab.pecas[0][1].jogador.cor=='branca' else 2) == False
assert tab.xequeMate(1 if tab.pecas[0][6].jogador.cor=='branca' else 2) == False
