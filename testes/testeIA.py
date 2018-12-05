from sys import *
path.append("../src")

from Tabuleiro import *
from IA import *

tab=Tabuleiro()
t=IA(tab)

assert t.get_melhor_jogada(2,True) != t.get_melhor_jogada(2,False)
