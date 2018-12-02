from IA import *
from Tabuleiro import *
import time


tabuleiro = Tabuleiro()
ia = IA(tabuleiro)

ti = time.clock()
ia.get_melhor_jogada(3, True)
print(time.clock() - ti)


