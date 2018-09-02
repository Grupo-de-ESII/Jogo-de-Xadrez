import Peca

class Bispo(Peca):
  def __init__(self,jogador):
    self.jogador=jogador
    
  def movimentosPossiveis(self,posicao,tabuleiro):
    l=[]
    (x,y)=posicao
    for i in [1,2,3,4,5,6,7]:
      #se movendo em direção ao canto superior direito
      if not tabuleiro.temPecaNaPosicao((x+1,y+1))
      or (tabuleiro.temPecaNaPosicao((x+1,y+1))
      and tabuleiro.playerPecaNaPosicao((x+1,y+1))!=jogador):
      
        
  
  def tipo(self):
    return 'bispo'
