import pygame
pygame.init()
screen=pygame.display.set_mode((500,300))
screen.fill('green')
isDone = True
while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
    pygame.display.update()
pygame.quit()