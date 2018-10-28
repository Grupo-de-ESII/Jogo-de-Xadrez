import pygame

#temporario --------------------------------------------------------
from Tabuleiro.Tabuleiro import Tabuleiro

pecasPretas = []
pecasBrancas = []

class uiPecaPreto(object):
    def __init__(self, posicao, tam, tipo):
        self.imagem = pygame.image.load("Ativos/"+tipo+"_preto.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        self.tipo = tipo;
        pecasPretas.append(self)

class uiPecaBranco(object):
    def __init__(self, posicao, tam, tipo):
        self.imagem = pygame.image.load("Ativos/"+tipo+"_branco.png")
        self.rect = pygame.Rect(posicao[0], posicao[1], tam, tam)
        self.tipo = tipo;
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
VERDE = [0,255,0]
BRANCAS = 1
PRETAS = 2

#Estados
TELA_INICIO = 0;
TELA_INTRO = 1;
TELA_MENU = 2;
TELA_OPCOES = 3;
TELA_JOGO = 4;

#imagens de fundo
imagem_menu1 = pygame.image.load("Ativos/menu_tela1.jpg")
imagem_menu2 = pygame.image.load("Ativos/menu_tela2.jpg")
imagem_opcoes = pygame.image.load("Ativos/opcoes_menu.png")
imagem_tabuleiro = pygame.image.load("Ativos/tabuleiromadeira.png")

#auxiliares
def desenha_menu1(tela):
    # Definido imagem de fundo da interface
    tela.blit(imagem_menu1, (0, 0))

    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito

#FUNÇÃO DESENHA_MENU2 PRECISA SER ORGANIZADAAAAAAA
def desenha_menu2(tela, estado):
    # Definido imagem de fundo da interface
    cor_texto = (255, 69, 0) #Cinza quase Branco
    cor_fundo = None #(115, 117, 117) #Cor estranha
    tela.blit(imagem_menu2, (0, 0)) #Define o background como imagem_menu2
    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito
    fonte_texto = pygame.font.Font("Ativos/Crackvetica.ttf", 60)
    if estado == TELA_INTRO:
        pygame.time.delay(3000)
        texto_jogar = fonte_texto.render('Jogar', True, cor_texto, cor_fundo)
        texto_opcoes = fonte_texto.render('Opcoes', True, cor_texto, cor_fundo)
        texto_sair = fonte_texto.render('Sair', True, cor_texto, cor_fundo)
        rect_jogar = texto_jogar.get_rect()
        rect_opcoes = texto_opcoes.get_rect()
        rect_sair = texto_sair.get_rect()
        rect_jogar.center = (450, 200)
        rect_opcoes.center = (450, 284)
        rect_sair.center = (450, 368)
        tela.blit(texto_jogar, rect_jogar)
        tela.blit(texto_opcoes, rect_opcoes)
        tela.blit(texto_sair, rect_sair)
    elif estado == TELA_MENU:
        texto_jogar = fonte_texto.render('Jogar', True, cor_texto, cor_fundo)
        texto_opcoes = fonte_texto.render('Opcoes', True, cor_texto, cor_fundo)
        texto_sair = fonte_texto.render('Sair', True, cor_texto, cor_fundo)
        rect_jogar = texto_jogar.get_rect()
        rect_opcoes = texto_opcoes.get_rect()
        rect_sair = texto_sair.get_rect()
        rect_jogar.center = (450, 200)
        rect_opcoes.center = (450, 284)
        rect_sair.center = (450, 368)
        tela.blit(texto_jogar, rect_jogar)
        tela.blit(texto_opcoes, rect_opcoes)
        tela.blit(texto_sair, rect_sair)
    pygame.display.update()
    #jogar = [239, 64] opcoes = [189, 64] sair = [159, 64]

#FUNÇÃO DESENHA_MENU2 PRECISA SER ORGANIZADAAAAAAA
def desenha_opcoes(tela):
    # Definido imagem de fundo da interface
    cor_texto = (255, 69, 0) #Cinza quase Branco
    cor_fundo = None #(115, 117, 117) #Cor estranha
    tela.blit(imagem_opcoes, (0, 0)) #Define o background como imagem_opcoes
    pygame.display.flip()  # Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update() # atualiza a tela com tudo que foi feito
    fonte_texto = pygame.font.Font("Ativos/Comical Smash.ttf", 60)
    texto_pecas = fonte_texto.render('Pecas:  Pretas X Brancas', True, cor_texto, cor_fundo)
    texto_dificuldade = fonte_texto.render('Dificuldade:  Facil x Dificil', True, cor_texto, cor_fundo)
    texto_voltar = fonte_texto.render('Voltar', True, cor_texto, cor_fundo)
    rect_pecas = texto_pecas.get_rect()
    rect_dificuldade = texto_dificuldade.get_rect()
    rect_voltar = texto_voltar.get_rect()
    rect_pecas.center = (450, 200)
    rect_dificuldade.center = (450, 284)
    rect_voltar.center = (450, 368)
    tela.blit(texto_pecas, rect_pecas)
    tela.blit(texto_dificuldade, rect_dificuldade)
    tela.blit(texto_voltar, rect_voltar)
    pygame.display.update()
    #jogar = [239, 64] opcoes = [189, 64] sair = [159, 64]

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
    desenha_menu2(tela, 1)

def desenha_tabuleiro(tela):
    tela.blit(imagem_tabuleiro, (0, 0))
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

def mover_peca(tela, peca, posicao):
    pos_x = peca.rect.x
    pos_y = peca.rect.y

    #afetam velocidade das peças
    velocidade = 5
    passo_x = L * velocidade
    passo_y = L * velocidade

    #serve para garantir igualdade entre máquinas de diferentes desempenhos
    dt = 0
    tempo_inicial = pygame.time.get_ticks() / 1000

    #descobre movimentacao
    if(pos_x < posicao[0]):
        if(pos_y == posicao[1]):
            passo_y = 0
        elif(pos_y > posicao[1]):
            passo_y = passo_y * (-1)
        while (pos_x < posicao[0]):
            pos_x += passo_x * dt
            pos_y += passo_y * dt
            peca.rect.x = pos_x
            peca.rect.y = pos_y
            desenha_tabuleiro(tela)

            tempo_final = pygame.time.get_ticks() / 1000
            dt = tempo_final - tempo_inicial
            tempo_inicial = tempo_final

    elif(pos_x == posicao[0]):
        passo_x = 0
        if(pos_y > posicao[1]):
            passo_y = passo_y * (-1)
            while (pos_y > posicao[1]):
                pos_x += passo_x * dt
                pos_y += passo_y * dt
                peca.rect.x = pos_x
                peca.rect.y = pos_y
                desenha_tabuleiro(tela)

                tempo_final = pygame.time.get_ticks() / 1000
                dt = tempo_final - tempo_inicial
                tempo_inicial = tempo_final
        else:
            while (pos_y < posicao[1]):
                pos_x += passo_x * dt
                pos_y += passo_y * dt
                peca.rect.x = pos_x
                peca.rect.y = pos_y
                desenha_tabuleiro(tela)

                tempo_final = pygame.time.get_ticks() / 1000
                dt = tempo_final - tempo_inicial
                tempo_inicial = tempo_final

    elif(pos_x > posicao[0]):
        passo_x = passo_x * (-1)
        if(pos_y == posicao[1]):
            passo_y = 0
        elif(pos_y > posicao[1]):
            passo_y = passo_y * (-1)
        while (pos_x > posicao[0]):
            pos_x += passo_x * dt
            pos_y += passo_y * dt
            peca.rect.x = pos_x
            peca.rect.y = pos_y
            desenha_tabuleiro(tela)

            tempo_final = pygame.time.get_ticks() / 1000
            dt = tempo_final - tempo_inicial
            tempo_inicial = tempo_final

    #Ajustando erros do DT
    peca.rect.x = posicao[0]
    peca.rect.y = posicao[1]
    desenha_tabuleiro(tela)
##########################################################################

#função principal

def interface():
    pygame.init()
    #JOGADOR1 FICA POR BAIXO
    jogador1=BRANCAS
    jogador2=PRETAS
    #funcao
    tab=Tabuleiro(1,2) #jogador 1 é branco, 2 é preto
    tela = pygame.display.set_mode((LARGURA,ALTURA)) #define tamanho da tela
    pygame.display.set_caption('Xadrez') #define título para tela


    jogador=[jogador1,jogador2]
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

    estado = TELA_INICIO
    desenha_menu1(tela)

    running = True
    while running:
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if estado == TELA_INICIO:
                if event.type == pygame.KEYDOWN:
                    #eletricidade(LARGURA, ALTURA, tela)
                    #estado = 1
                    estado = TELA_MENU
                    desenha_menu2(tela,estado)

            if estado == TELA_INTRO or estado == TELA_MENU: #estado 3 precisa ser removido daqui ou acertado
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos) #usado para debugar
                    if ((pos[0]>= 332 and pos[0]<= 569.5) and (pos[1] >= 168 and pos[1] <= 220)): #detecta "JOGAR"
                        estado = TELA_JOGO

                        # def __init__(self, posicao, tam, tipo):
                        if (jogador1 == 1):
                            uiPecaPreto(dic["A7"], L, "peao")
                            uiPecaPreto(dic["B7"], L, "peao")
                            uiPecaPreto(dic["C7"], L, "peao")
                            uiPecaPreto(dic["D7"], L, "peao")
                            uiPecaPreto(dic["E7"], L, "peao")
                            uiPecaPreto(dic["F7"], L, "peao")
                            uiPecaPreto(dic["G7"], L, "peao")
                            uiPecaPreto(dic["H7"], L, "peao")
                            uiPecaPreto(dic["C8"], L, "bispo")
                            uiPecaPreto(dic["F8"], L, "bispo")
                            uiPecaPreto(dic["A8"], L, "torre")
                            uiPecaPreto(dic["H8"], L, "torre")
                            uiPecaPreto(dic["B8"], L, "cavalo")
                            uiPecaPreto(dic["G8"], L, "cavalo")
                            uiPecaPreto(dic["D8"], L, "rei")
                            uiPecaPreto(dic["E8"], L, "rainha")

                            uiPecaBranco(dic["A2"], L, "peao")
                            uiPecaBranco(dic["B2"], L, "peao")
                            uiPecaBranco(dic["C2"], L, "peao")
                            uiPecaBranco(dic["D2"], L, "peao")
                            uiPecaBranco(dic["E2"], L, "peao")
                            uiPecaBranco(dic["F2"], L, "peao")
                            uiPecaBranco(dic["G2"], L, "peao")
                            uiPecaBranco(dic["H2"], L, "peao")
                            uiPecaBranco(dic["C1"], L, "bispo")
                            uiPecaBranco(dic["F1"], L, "bispo")
                            uiPecaBranco(dic["B1"], L, "cavalo")
                            uiPecaBranco(dic["G1"], L, "cavalo")
                            uiPecaBranco(dic["A1"], L, "torre")
                            uiPecaBranco(dic["H1"], L, "torre")
                            uiPecaBranco(dic["D1"], L, "rei")
                            uiPecaBranco(dic["E1"], L, "rainha")
                        else:
                            uiPecaBranco(dic["A7"], L, "peao")
                            uiPecaBranco(dic["B7"], L, "peao")
                            uiPecaBranco(dic["C7"], L, "peao")
                            uiPecaBranco(dic["D7"], L, "peao")
                            uiPecaBranco(dic["E7"], L, "peao")
                            uiPecaBranco(dic["F7"], L, "peao")
                            uiPecaBranco(dic["G7"], L, "peao")
                            uiPecaBranco(dic["H7"], L, "peao")
                            uiPecaBranco(dic["C8"], L, "bispo")
                            uiPecaBranco(dic["F8"], L, "bispo")
                            uiPecaBranco(dic["A8"], L, "torre")
                            uiPecaBranco(dic["H8"], L, "torre")
                            uiPecaBranco(dic["B8"], L, "cavalo")
                            uiPecaBranco(dic["G8"], L, "cavalo")
                            uiPecaBranco(dic["D8"], L, "rei")
                            uiPecaBranco(dic["E8"], L, "rainha")

                            uiPecaPreto(dic["A2"], L, "peao")
                            uiPecaPreto(dic["B2"], L, "peao")
                            uiPecaPreto(dic["C2"], L, "peao")
                            uiPecaPreto(dic["D2"], L, "peao")
                            uiPecaPreto(dic["E2"], L, "peao")
                            uiPecaPreto(dic["F2"], L, "peao")
                            uiPecaPreto(dic["G2"], L, "peao")
                            uiPecaPreto(dic["H2"], L, "peao")
                            uiPecaPreto(dic["C1"], L, "bispo")
                            uiPecaPreto(dic["F1"], L, "bispo")
                            uiPecaPreto(dic["B1"], L, "cavalo")
                            uiPecaPreto(dic["G1"], L, "cavalo")
                            uiPecaPreto(dic["A1"], L, "torre")
                            uiPecaPreto(dic["H1"], L, "torre")
                            uiPecaPreto(dic["D1"], L, "rei")
                            uiPecaPreto(dic["E1"], L, "rainha")
                        desenha_tabuleiro(tela)

                    if ((pos[0]>= 304.5 and pos[0]<= 594.5) and (pos[1] >= 252 and pos[1] <= 308)): #detecta "OPCOES"
                        estado = TELA_OPCOES
                        desenha_opcoes(tela)
                    if ((pos[0]>= 370.5 and pos[0]<= 529.5) and (pos[1] >= 336 and pos[1] <= 392)): #detecta "SAIR"
                          running = False

            if estado == TELA_OPCOES:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)  # usado para debugar
                    if ((pos[0]>= 309 and pos[0]<= 503.5) and (pos[1] >= 168.5 and pos[1] <= 218)): #detecta "PRETAS"
                        jogador1 = PRETAS
                        jogador2 = BRANCAS
                        print("PRETAS")
                    if ((pos[0]>= 578 and pos[0]<= 797.5) and (pos[1] >= 168.5 and pos[1] <= 218)): #detecta "BRANCAS"
                        jogador1 = BRANCAS
                        jogador2 = PRETAS
                        print("BRANCAS")
                    if ((pos[0]>= 355.5 and pos[0]<= 545.5) and (pos[1] >= 336 and pos[1] <= 385)): #detecta "VOLTAR"
                        estado = TELA_MENU
                        desenha_menu2(tela,estado)

            if estado == TELA_JOGO:
                # (x[0] // 60 * 60, x[1] // 60 * 60)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    pos_peca = (pos[0] // 60 * 60, pos[1] // 60 * 60)
                    for peca in pecasPretas:
                        if peca.rect.x == pos_peca[0] and peca.rect.y == pos_peca[1]:
                            print(peca)
                            print(peca.tipo)
                    for peca in pecasBrancas:
                        if peca.rect.x == pos_peca[0] and peca.rect.y == pos_peca[1]:
                            print(peca)
                            print(peca.tipo)

                if key[pygame.K_p]:
                    print(pecasBrancas)
                    print(pecasPretas)
                    mover_peca(tela, pecasPretas[0], dic["E3"])  # Peao petro A7
                    mover_peca(tela, pecasBrancas[0], dic["C4"])  # Peao branco A2
                    mover_peca(tela, pecasPretas[0], dic["A7"])  # Peao petro A7
                    mover_peca(tela, pecasBrancas[0], dic["A2"])  # Peao branco A2

                if key[pygame.K_c]:
                    mover_peca(tela, pecasPretas[12], dic["B6"])  # Cavalo preto B8
                    mover_peca(tela, pecasPretas[12], dic["C6"])

    pygame.display.quit()
    pygame.quit()

interface()