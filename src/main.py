import Tabuleiro,Jogador

from IA import *
import time

#dont polute here with a lot of global variables.
#make KISS, create a class with constants if needed


#I don't need to say that to Luis or Julia, but Wallace,
#dont do mess


#import GRAPHICS_THING

#graphics init


ia = IA()

ti = time.clock()
ia.get_melhor_jogada(True)
print(time.clock() - ti)


