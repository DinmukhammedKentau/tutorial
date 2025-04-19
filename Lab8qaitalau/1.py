import pygame
pygame.init()
screen=pygame.display.set_mode((600,800))
pygame.display.set_caption("Snake")
running = True
color=(255,255,255)
rect=pygame.Rect(0,0,100,100)
while running:
    pygame.draw.rect(screen,color,rect,1)#1 деген калындыгы деген соз

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
           pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if color==(255,255,255):
                    color=(255,0,0)
                else:
                    color=(255,255,255)
    pygame.display.flip()
