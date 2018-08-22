import pygame


def interface():
    pygame.init()
    BRANCO = (255,255,255)
    MARROM = (139,69,19)
    info = pygame.display.Info() #cria objeto do Info com atributos da tela
    tam_w = info.current_w/10
    tam_h = info.current_h/10

    tela = pygame.display.set_mode((info.current_w,info.current_h)) #define tamanho da tela
    pygame.display.set_caption('Xadrez') #define título para tela
    #Pinta tela
    for i in range(1,8):
        for j in range(1,8):
            if(i%2!=0):
                if(j%2==0):
                    pygame.draw.rect(tela, MARROM,
                                     [i * tam_w, j * tam_h, tam_w, tam_h])
                else:
                    pygame.draw.rect(tela, BRANCO,
                                     [i * tam_w, j * tam_h, tam_w, tam_h])
            else:
                if (j % 2 == 0):
                    pygame.draw.rect(tela, BRANCO,
                                     [i * tam_w, j * tam_h, tam_w, tam_h])
                else:
                    pygame.draw.rect(tela, MARROM,
                                     [i * tam_w, j * tam_h, tam_w, tam_h])

    #minhafonte = pygame.font.SysFont('Comic Sans MS', 30)
    #textsurface = minhafonte.render('Omelette au fromage', False, BRANCO)
    #tela.blit(textsurface, (0, 0))
    pygame.display.flip() #Por algum motivo isso é necessário quando se usa um draw no pygame
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()

interface()