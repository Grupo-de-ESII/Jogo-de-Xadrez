# This file declares the Board Class, that contain the Pieces
# and is a high-level interface to the user use the piece


from copy import *
from Peca.Peca import *
from Jogador.Jogador import *

class Tabuleiro:
    def __init__(self):
        self.pecas = [[None for j in range(8)] for i in range(8)]
        self.pilha = []

        self.jogador_1 = Jogador('branca')
        self.jogador_2 = Jogador('preta')

        for i in range(8):
            self.pecas[i][1] = Peao(self.jogador_1)
        self.pecas[0][0] = Torre(self.jogador_1)
        self.pecas[1][0] = Cavalo(self.jogador_1)
        self.pecas[2][0] = Bispo(self.jogador_1)
        self.pecas[3][0] = Rei(self.jogador_1)
        self.pecas[4][0] = Rainha(self.jogador_1)
        self.pecas[5][0] = Bispo(self.jogador_1)
        self.pecas[6][0] = Cavalo(self.jogador_1)
        self.pecas[7][0] = Torre(self.jogador_1)

        for i in range(8):
            self.pecas[i][6] = Peao(self.jogador_2)
        self.pecas[0][7] = Torre(self.jogador_2)
        self.pecas[1][7] = Cavalo(self.jogador_2)
        self.pecas[2][7] = Bispo(self.jogador_2)
        self.pecas[3][7] = Rei(self.jogador_2)
        self.pecas[4][7] = Rainha(self.jogador_2)
        self.pecas[5][7] = Bispo(self.jogador_2)
        self.pecas[6][7] = Cavalo(self.jogador_2)
        self.pecas[7][7] = Torre(self.jogador_2)

    def possiveisMovimentos(self):
        l = []
        for i in range(8):
            for j in range(8):
                if self.pecas[i][j] is not None:
                    l = l + self.pecas[i][j].movimentosPossiveis((i, j), self)
        return l

    def pecaPossiveisMovimentos(self, posicao):
        (i, j) = posicao
        if self.pecas[i][j] is not None:
            return self.pecas[i][j].movimentosPossiveis((i, j), self)
        return []

    def tipoPecaNaPosicao(self, posicao):
        (x, y) = posicao
        if self.pecas[x][y] is not None:
            return self.pecas[x][y].tipo()
        return ''

    def temPecaNaPosicao(self, posicao):
        (x, y) = posicao
        return 0 <= x <= 7 and 0 <= y <= 7 and self.pecas[x][y] is not None

    def avalia(self, heuristica):
        return heuristica(self.pecas)

    # private methods, don't call
    # thanks to python by don't have private methods

    def indexFromColumn(self, i):
        return chr(i + ord('A'))

    def playerPecaNaPosicao(self, posicao):
        (x, y) = posicao
        if (self.pecas[x][y] is not None):
            return self.pecas[x][y].jogador
        return None

    def pieceFromIndex(self, i):
        l = ['torre', 'cavalo', 'bispo', 'rainha', 'rei', 'bisto', 'cavalo', 'rook']
        return l[i]

    def getiPos(self, a):
        l = []
        for i in a:
            l.append(i[0][2])
        return l

    def matrix2str(self, posicao):
        (x, y) = posicao
        return self.indexFromColumn(x) + str(y + 1)

    def str2matrix(self, str):
        return (ord(str[0]) - ord('A'), int(str[1]) - 1)

    def move(self, posicao1, posicao2):  # móve
        (xi, yi) = posicao1
        (xf, yf) = posicao2
        if yf < 0 or yf > 7:
            return
        tmp = self.pecas[xi][yi]
        self.pecas[xi][yi] = None
        self.pecas[xf][yf] = tmp

    def falsoMovimento(self, posicao1, posicao2):
        self.pilha.append(deepcopy(self.pecas))
        self.move(posicao1, posicao2)

    def reset(self):
        self.pecas = self.pilha[-1]
        self.pilha = self.pilha[0:-1]