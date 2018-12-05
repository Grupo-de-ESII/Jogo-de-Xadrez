# This file declares the Board Class, that contain the Pieces
# and is a high-level interface to the user use the piece


from copy import *
from Peca import *
from Jogador import *

class Tabuleiro:
    def __init__(self):
        self.pecas = [[None for j in range(8)] for i in range(8)]
        self.pilha = []

        self.player1 = Jogador('branca')
        self.player2 = Jogador('preta')
        self.posicaoReis={self.player1:(4,0),self.player2:(4,7)}
        for i in range(8):
            self.pecas[i][1] = Peao(self.player1)
        self.pecas[0][0] = Torre(self.player1)
        self.pecas[1][0] = Cavalo(self.player1)
        self.pecas[2][0] = Bispo(self.player1)
        self.pecas[3][0] = Rainha(self.player1)
        self.pecas[4][0] = Rei(self.player1)
        self.pecas[5][0] = Bispo(self.player1)
        self.pecas[6][0] = Cavalo(self.player1)
        self.pecas[7][0] = Torre(self.player1)

        for i in range(8):
            self.pecas[i][6] = Peao(self.player2)
        self.pecas[0][7] = Torre(self.player2)
        self.pecas[1][7] = Cavalo(self.player2)
        self.pecas[2][7] = Bispo(self.player2)
        self.pecas[3][7] = Rainha(self.player2)
        self.pecas[4][7] = Rei(self.player2)
        self.pecas[5][7] = Bispo(self.player2)
        self.pecas[6][7] = Cavalo(self.player2)
        self.pecas[7][7] = Torre(self.player2)
        self.contadorRodadas=0

    def possiveisMovimentos(self):
        l = []
        for i in range(8):
            for j in range(8):
                l=l+self.pecaPossiveisMovimentos((i,j))
        return l
    
    #baseado em http://soxadrez.com.br/conteudos/fases_partida/
    def empate(self,vezDe):
        return self.afogamento(vezDe) or self.tresPosicoes() or self.cinquentaMovimentos() or self.insuficienciaMaterial()
    def afogamento(self,vezDe):
        return self.jogadorPossiveisMovimentos(vezDe) == []
    def tresPosicoes(self):
        return False
    def cinquentaMovimentos(self):
        return self.contadorRodadas >= 50
    def insuficienciaMaterial(self):
        hash1={}
        hash2={}
        for i in range(8):
            for j in range(8):
                if self.pecas[i][j] is not None:
                    if(self.pecas[i][j].jogador==self.player1):
                        hash1[self.pecas[i][j].tipo()]=0 if self.pecas[i][j].tipo() not in hash1 else hash1[self.pecas[i][j].tipo()]+1
                    else:
                        hash2[self.pecas[i][j].tipo()]=0 if self.pecas[i][j].tipo() not in hash2 else hash2[self.pecas[i][j].tipo()]+1
        l1=hash1.keys()
        l2=hash2.keys()
        p1Suficiente=('rei' in l1 and 'rainha' in l1) or ('rei' in l1 and 'torre' in l1) or ('rei' in l1 and 'bispo' in l1 and 'cavalo' in l1) or ('rei' in l1 and 'bispo' in l1 and hash1['bispo'] == 2)
        p2Suficiente=('rei' in l2 and 'rainha' in l2) or ('rei' in l2 and 'torre' in l2) or ('rei' in l2 and 'bispo' in l2 and 'cavalo' in l2) or ('rei' in l2 and 'bispo' in l2 and hash2['bispo'] == 2)
        return not (p1Suficiente or p2Suficiente)
    def xequeMate(self, cor):
        #BRANCAS = 1 ; PRETAS = 2
        return self.jogadorPossiveisMovimentos(Jogador('branca' if cor==1 else 'preta'))==[]

    def jogadorPossiveisMovimentos(self,jogador):
        l=self.possiveisMovimentos()
        aux=[]
        for i in l:
            pos=i[0][1]
            (posx,posy)=pos
            if(self.pecas[posx][posy].jogador.cor==jogador.cor):
                aux.append(i)
        return aux
    def pecaPossiveisMovimentos(self, posicao):
        (i, j) = posicao
        if self.pecas[i][j] is not None:
            meuTipo=self.pecas[i][j].tipo()
            l=self.pecas[i][j].movimentosPossiveis((i, j), self)
#            print("Movimentos antes do tratamento : " + str(l))
            posicaoMeuRei=self.posicaoReis[self.pecas[i][j].jogador]
            meuRei=self.pecas[posicaoMeuRei[0]][posicaoMeuRei[1]]
            aux=[]
            for jogada in l:
                self.falsoMovimento(jogada[0][1],jogada[0][2])
                if(meuTipo != 'rei' and not meuRei.estouEmXeque(posicaoMeuRei,self)):
                    aux.append(jogada)
                if(meuTipo == 'rei' and not meuRei.estouEmXeque(jogada[0][2],self)):
                    aux.append(jogada)
                self.reset()
            return aux
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
        tmp = self.pecas[xi][yi]
        self.pecas[xi][yi] = None
        backup=self.pecas[xf][yf]
        self.pecas[xf][yf] = tmp
        if(self.pecas[xf][yf].tipo() == 'peao'):
            self.pecas[xf][yf].primeiroMovimento=False
        elif(self.pecas[xf][yf].tipo() == 'rei'):
            self.pecas[xf][yf].jaMeMovi=True
            self.posicaoReis[self.pecas[xf][yf].jogador]=(xf,yf)
        if self.pecas[xf][yf].tipo() == 'peao' or backup is not None:
            self.contadorRodadas=-1 #quando incrementar ali embaixo vira 0
        self.contadorRodadas=self.contadorRodadas+1

    def falsoMovimento(self, posicao1, posicao2):
        self.pilha.append((self.pecas,self.posicaoReis,self.contadorRodadas))
        self.pecas=deepcopy(self.pecas)
        self.posicaoReis={}
        for i in range(8):
            for j in range(8):
                if((self.pecas[i][j] is not None) and self.pecas[i][j].tipo()=='rei'):
                    self.posicaoReis[self.pecas[i][j].jogador]=(i,j)
        self.move(posicao1, posicao2)

    def reset(self):
        (self.pecas,self.posicaoReis,self.contadorRodadas) = self.pilha[-1]
        self.pilha = self.pilha[0:-1]

    def __str__(self):
        s=""
        l=len(self.pecas)
        for i in range(l):
            for j in range(l):
                s=s+" " + str(self.pecas[i][j].tipo() if self.pecas[i][j] is not None else "    ")
            s=s+"\n"
        return s
    def jogadaSimples(self,jogada):
        pass
