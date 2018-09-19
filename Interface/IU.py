import pygame

#temporario --------------------------------------------------------
pecasPretas = []
pecasBrancas = []

class peaoPreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/peao_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class bispoPreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/bispo_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class cavaloPreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/cavalo_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class torrePreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/torre_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class rainhaPreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/rainha_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class reiPreto(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/rei_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasPretas.append(self)

class peaoBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/peao_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)

class bispoBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/bispo_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)

class cavaloBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/cavalo_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)

class torreBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/torre_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)

class rainhaBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/rainha_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)

class reiBranco(object):
    def __init__(self, posicao, tam):
        self.imagem = pygame.image.load("Ativos/rei_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        pecasBrancas.append(self)
##########################################################################

# info
LARGURA = 900
ALTURA = 600
L = ALTURA // 10  # Unidadade mínima da tela, L = lado de um quadrado do tabuleiro

# Cores
BRANCO = [255,255,255]
CINZA = [100, 100, 100] # [139,69,19]
AMARELO = [255,255,0]

#auxiliares
def desenha_menu1(tela):
    # Definido imagem de fundo da interface
    img = pygame.image.load("Ativos/menu_tela1.jpg")
    tela.blit(img, (0, 0))

    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito

#FUNÇÃO DESENHA_MENU2 PRECISA SER ORGANIZADAAAAAAA
def desenha_menu2(tela):
    # Definido imagem de fundo da interface
    img = pygame.image.load("Ativos/menu_tela2.jpg")
    tela.blit(img, (0, 0))
    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito
    pygame.time.delay(3000)
    fontezinha = pygame.font.Font("Ativos/Crackvetica.ttf", 60)
    textSurfaceObj = fontezinha.render('Jogar', True, (240, 240, 240), (115, 117, 117))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (390, 240)
    tela.blit(textSurfaceObj, textRectObj)
    pygame.display.update()

#função da tela inicial -> efeito de eletricidade
def eletricidade(largura, altura, tela):
    eletricidade = pygame.Surface((largura, altura))
    eletricidade.fill((255,255,255))
    pygame.mixer.music.load("Ativos/electricshock.mp3")
    pygame.mixer.music.play(-1)
    for alpha in range(0, 300):
        eletricidade.set_alpha(alpha)
        desenha_menu1(tela)
        tela.blit(eletricidade, (0,0))
        pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ativos/thunder2.mp3")
    pygame.mixer.music.play(0)
    desenha_menu2(tela)

def desenha_tabuleiro(tela):
    # Definido imagem de fundo da interface
    img = pygame.image.load("Ativos/tabuleiromadeira.png")
    tela.blit(img, (0, 0))

    # Pinta tabuleiro
    for i in range(0, 8):
        for j in range(0, 8):
            if (i % 2 != 0):
                if (j % 2 == 0):
                    pygame.draw.rect(tela, CINZA,
                                     [i * L + 3 * L, j * L + L, L, L])  # [POS_X, POS_Y, LARGURA, ALTURA]
                else:
                    pygame.draw.rect(tela, BRANCO,
                                     [i * L + 3 * L, j * L + L, L, L])  # [POS_X, POS_Y, LARGURA, ALTURA]
            else:
                if (j % 2 == 0):
                    pygame.draw.rect(tela, BRANCO,
                                     [i * L + 3 * L, j * L + L, L, L])  # [POS_X, POS_Y, LARGURA, ALTURA]
                else:
                    pygame.draw.rect(tela, CINZA,
                                     [i * L + 3 * L, j * L + L, L, L])  # [POS_X, POS_Y, LARGURA, ALTURA]

    # Pinta dois quadrados amarelos do lado do tabuleiro
    pygame.draw.rect(tela, AMARELO, [L // 2, L, 2 * L, 8 * L])
    pygame.draw.rect(tela, AMARELO, [11 * L + (L // 2), L, 2 * L, 8 * L])

    # COLOCA PECAS NA TELA
    for peca in pecasBrancas:
        tela.blit(peca.imagem, peca.rect)
    for peca in pecasPretas:
        tela.blit(peca.imagem, peca.rect)

    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito

def moverPeca(tela, peca, posicao):
    pos_x = peca.rect.x
    pos_y = peca.rect.y
    passo = 6
    if(pos_x < posicao[0]):
        if(pos_y < posicao[1]):
            while(pos_x < posicao[0]):
                pos_x += passo
                pos_y += passo
                peca.rect.x = pos_x
                peca.rect.y = pos_y
                desenha_tabuleiro(tela)
##########################################################################

#função principal

def interface():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA,ALTURA)) #define tamanho da tela
    pygame.display.set_caption('Xadrez') #define título para tela

    #negolossauroRex
    dic = {
        "A8" : [3*L, L], "B8": [4*L, L], "C8": [5*L, L], "D8": [6*L, L],
        "E8": [7*L, L], "F8": [8*L, L], "G8": [9*L, L], "H8": [10*L, L],
        "A7": [3*L, 2*L], "B7": [4*L, 2*L], "C7": [5*L, 2*L], "D7": [6*L, 2*L],
        "E7": [7*L, 2*L], "F7": [8*L, 2*L], "G7": [9*L, 2*L], "H7": [10*L, 2*L],
        "A6": [3*L, 3*L], "B6": [4*L, 3*L], "C6": [5*L, 3*L], "D6": [6*L, 3*L],
        "E6": [7*L, 3*L], "F6": [8*L, 3*L], "G6": [9*L, 3*L], "H6": [10*L, 3*L],
        "A5": [3*L, 4*L], "B5": [4*L, 4*L], "C5": [5*L, 4*L], "D5": [6*L, 4*L],
        "E5": [7*L, 4*L], "F5": [8*L, 4*L], "G5": [9*L, 4*L], "H5": [10*L, 4*L],
        "A4": [3*L, 5*L], "B4": [4*L, 5*L], "C4": [5*L, 5*L], "D4": [6*L, 5*L],
        "E4": [7*L, 5*L], "F4": [8*L, 5*L], "G4": [9*L, 5*L], "H4": [10*L, 5*L],
        "A3": [3*L, 6*L], "B3": [4*L, 6*L], "C3": [5*L, 6*L], "D3": [6*L, 6*L],
        "E3": [7*L, 6*L], "F3": [8*L, 6*L], "G3": [9*L, 6*L], "H3": [10*L, 6*L],
        "A2": [3*L, 7*L], "B2": [4*L, 7*L], "C2": [5*L, 7*L], "D2": [6*L, 7*L],
        "E2": [7*L, 7*L], "F2": [8*L, 7*L], "G2": [9*L, 7*L], "H2": [10*L, 7*L],
        "A1": [3*L, 8*L], "B1": [4*L, 8*L], "C1": [5*L, 8*L], "D1": [6*L, 8*L],
        "E1": [7*L, 8*L], "F1": [8*L, 8*L], "G1": [9*L, 8*L], "H1": [10*L, 8*L],
    }

    #CRIA OBJETOS DAS PEÇAS
    peaoPreto(dic["A7"], L)
    peaoPreto(dic["B7"], L)
    peaoPreto(dic["C7"], L)
    peaoPreto(dic["D7"], L)
    peaoPreto(dic["E7"], L)
    peaoPreto(dic["F7"], L)
    peaoPreto(dic["G7"], L)
    peaoPreto(dic["H7"], L)
    bispoPreto(dic["C8"], L)
    bispoPreto(dic["F8"], L)
    torrePreto(dic["A8"], L)
    torrePreto(dic["H8"], L)
    cavaloPreto(dic["B8"], L)
    cavaloPreto(dic["G8"], L)
    reiPreto(dic["D8"], L)
    rainhaPreto(dic["E8"], L)
    peaoBranco(dic["A2"], L)
    peaoBranco(dic["B2"], L)
    peaoBranco(dic["C2"], L)
    peaoBranco(dic["D2"], L)
    peaoBranco(dic["E2"], L)
    peaoBranco(dic["F2"], L)
    peaoBranco(dic["G2"], L)
    peaoBranco(dic["H2"], L)
    bispoBranco(dic["C1"], L)
    bispoBranco(dic["F1"], L)
    cavaloBranco(dic["B1"], L)
    cavaloBranco(dic["G1"], L)
    torreBranco(dic["A1"], L)
    torreBranco(dic["H1"], L)
    reiBranco(dic["D1"], L)
    rainhaBranco(dic["E1"], L)

    estado = 0
    desenha_menu1(tela)

    running = True
    while running:
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            moverPeca(tela, pecasPretas[0], dic["E3"])
        if key[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if estado == 0:
                if event.type == pygame.KEYDOWN:
                    eletricidade(LARGURA, ALTURA, tela)
                    estado += 1
    pygame.display.quit()
    pygame.quit()

interface()