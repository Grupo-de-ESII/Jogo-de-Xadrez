import pygame

def interface():
    pygame.init()
    tela = pygame.display.set_mode((300,300))
    pygame.display.set_caption('Xadrez')
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Omelette au fromage', False, (255,255,255))
    tela.blit(textsurface, (0,0))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()

interface()