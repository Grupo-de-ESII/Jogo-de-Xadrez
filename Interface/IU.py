import pygame

def interface():
    pygame.init()
    info = pygame.display.Info() #cria objeto do Info com atributos da tela
    tela = pygame.display.set_mode((info.current_w,info.current_h)) #define tamanho da tela
    pygame.display.set_caption('Xadrez') #define título para tela
    minhafonte = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = minhafonte.render('Omelette au fromage', False, (255,255,255))
    tela.blit(textsurface, (0, 0))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()

interface()