import pygame

pygame.init()
screen = pygame.display.set_mode((500, 200))
defaultFon = (252, 186, 3)
screen.fill(defaultFon)
isDone = True
while isDone:

    screen.fill(defaultFon)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            isDone = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                defaultFon = (19, 247, 15)

