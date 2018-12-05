from sys import *

path.append("../src/")

from Tabuleiro import *

tab=Tabuleiro()

d={'branca':1, 'preta':2}

#XequeMate não explode no começo
assert tab.xequeMate(d[tab.pecas[0][0].jogador.cor]) == False
assert tab.xequeMate(d[tab.pecas[0][7].jogador.cor]) == False
jog=tab.pecas[0][1].jogador

#vendo se deixa algum lixo que torne o proximo xequeMate explodir
tab.falsoMovimento((0,1),(0,3))
tab.reset()

assert tab.xequeMate(d[tab.pecas[0][0].jogador.cor]) == False
assert tab.xequeMate(d[tab.pecas[0][7].jogador.cor]) == False
assert tab.pecas[0][1] is not None
assert tab.pecas[0][1].jogador == jog


#agora é para valer
tab.move((0,1),(0,3))
assert tab.xequeMate(d[tab.pecas[0][0].jogador.cor]) == False
assert tab.xequeMate(d[tab.pecas[0][7].jogador.cor]) == False

reiBranco=tab.posicaoReis[tab.pecas[0][0].jogador]
reiPreto=tab.posicaoReis[tab.pecas[0][7].jogador]
assert tab.pecaPossiveisMovimentos(reiBranco) == []
assert tab.pecaPossiveisMovimentos(reiPreto) == []
