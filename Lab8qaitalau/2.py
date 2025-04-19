import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
screen.fill((255,255,255))
running=True
clock=pygame.time.Clock()#FPS орнату ушин
x,y=10,10
while running:

    screen.fill((255,255,255))
    center=(x,y)

    pygame.draw.circle(screen,(255,0,0),center,10)

    x += 10
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         pygame.quit()
         running=False

    pygame.display.flip()
    clock.tick(60)#FPS орнату ушин