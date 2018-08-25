import pygame


def interface():
    pygame.init()

    # Cores
    BRANCO = [255,255,255]
    CINZA = [100, 100, 100] # [139,69,19]
    AMARELO = [255,255,0]

    info = pygame.display.Info() # cria objeto do Info com atributos da tela

    L = info.current_h // 10  # Unidadade mínima da tela, L = lado de um quadrado do tabuleiro

    tela = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN) #define tamanho da tela
    pygame.display.set_caption('Xadrez') #define título para tela
    #Pinta tela
    #tela.fill([255,255,255])

    # Definido imagem de fundo da interface
    img = pygame.image.load("Ativos/tabuleiromadeira.png")
    tela.blit(img,(0,0))

    # Pinta tabuleiro
    for i in range(0,8):
        for j in range(0,8):
            if(i%2!=0):
                if(j%2==0):
                    pygame.draw.rect(tela, CINZA,
                                     [i * L + L, j * L + L, L, L]) #[POS_X, POS_Y, LARGURA, ALTURA]
                else:
                    pygame.draw.rect(tela, BRANCO,
                                     [i * L + L, j * L + L, L, L]) #[POS_X, POS_Y, LARGURA, ALTURA]
            else:
                if (j % 2 == 0):
                    pygame.draw.rect(tela, BRANCO,
                                     [i * L + L, j * L + L, L, L]) #[POS_X, POS_Y, LARGURA, ALTURA]
                else:
                    pygame.draw.rect(tela, CINZA,
                                     [i * L + L, j * L + L, L, L]) #[POS_X, POS_Y, LARGURA, ALTURA]

    # Pinta o lado do tabuleiro de branco
    pygame.draw.rect(tela, BRANCO, [10 * L, 0, info.current_w - 10 * L, info.current_w])

    # Pinta dois quadrados amarelos do lado do tabuleiro
    pygame.draw.rect(tela, AMARELO, [10.5 * L, 0.5 * L, 4 * L, 4 * L])
    pygame.draw.rect(tela, AMARELO, [10.5 * L, 11 * 0.5 * L, 4 * L, 4 * L])

    #minhafonte = pygame.font.SysFont('Comic Sans MS', 30)
    #textsurface = minhafonte.render('Omelette au fromage', False, BRANCO)
    #tela.blit(textsurface, (0, 0))
    pygame.display.flip() #Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update()
    running = True
    while running:

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()

interface()