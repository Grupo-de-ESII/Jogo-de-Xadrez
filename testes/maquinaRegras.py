import sys

sys.path.append("../src")

from Tabuleiro import Tabuleiro


t=Tabuleiro()
#brancas
assert t.tipoPecaNaPosicao((0,0)) == 'torre'
assert t.tipoPecaNaPosicao((7,0)) == 'torre'
assert t.tipoPecaNaPosicao((1,0)) == 'cavalo'
assert t.tipoPecaNaPosicao((6,0)) == 'cavalo'
assert t.tipoPecaNaPosicao((2,0)) == 'bispo'
assert t.tipoPecaNaPosicao((5,0)) == 'bispo'
assert t.tipoPecaNaPosicao((3,0)) == 'rainha'
assert t.tipoPecaNaPosicao((4,0)) == 'rei'

for i in [0,1,2,3,4,5,6,7]:
	assert t.tipoPecaNaPosicao((i,1))=='peao'
#pretas
assert t.tipoPecaNaPosicao((0,7)) == 'torre'
assert t.tipoPecaNaPosicao((7,7)) == 'torre'
assert t.tipoPecaNaPosicao((1,7)) == 'cavalo'
assert t.tipoPecaNaPosicao((6,7)) == 'cavalo'
assert t.tipoPecaNaPosicao((2,7)) == 'bispo'
assert t.tipoPecaNaPosicao((5,7)) == 'bispo'
assert t.tipoPecaNaPosicao((3,7)) == 'rainha'
assert t.tipoPecaNaPosicao((4,7)) == 'rei'
for i in [0,1,2,3,4,5,6,7]:
	assert t.tipoPecaNaPosicao((i , 6)) == 'peao'
