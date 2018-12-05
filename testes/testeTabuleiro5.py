from sys import *
path.append("../src")

from Tabuleiro import *

tab=Tabuleiro()

tab.falsoMovimento((0,1),(0,3))
tab.possiveisMovimentos()
tab.reset()
