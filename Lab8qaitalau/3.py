import pygame
pygame.init()
screen=pygame.display.set_mode((100,100))
x=0
y=0
running=True
while running:

    screen.fill((255, 255, 255))
    RECT = pygame.draw.rect(screen, (255, 0, 0), (x, y, 20, 20))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running=False
          pygame.quit()
      if event.type == pygame.KEYDOWN:

          if event.key == pygame.K_UP:
              if y==-10:
                  y=90

              else:
               y-=10
          if event.key==pygame.K_DOWN:
              if y==90:
                  y=0
              else:y+=10
          if event.key==pygame.K_LEFT:
              if x==-10:
                  x=90
              x-=10
          if event.key == pygame.K_RIGHT:
              if x==90:
                  x=0
              x+=10
    pygame.display.flip()