import Peca

class Bispo(Peca):
  def __init__(self,jogador):
    self.jogador=jogador
    
  def movimentosPossiveis(self,posicao,tabuleiro):
    l=[]
    (x,y)=posicao
    for i in [1,2,3,4,5,6,7]:
      #se movendo em direção ao canto superior direito na visão das brancas
      if (x+i)>7 or (y+i)>7:
        break;
      if not tabuleiro.temPecaNaPosicao((x+i,y+i)):
        l.append([['bispo',posicao,(x+i,y+i)]])
      elif tabuleiro.playerPecaNaPosicao((x+i,y+i))!=jogador):
        l.append([['bispo',posicao,(x+i,y+i)]])
        
    
    return l
      
        
  
  def tipo(self):
    return 'bispo'
