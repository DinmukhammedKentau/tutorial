import pygame
import time
pygame.init()
screen=pygame.display.set_mode((960,1280))


mainCoordinateX=250
mainCoordinateY=250
isDone=True
while isDone:

    screen.fill((255,255,255))
    pygame.draw.circle(screen,"Red",(mainCoordinateX,mainCoordinateY),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if mainCoordinateY-20-25>0:
                 mainCoordinateY-=20
                else :
                     image=pygame.image.load(r"C:\Users\Dimash\Desktop\fd452307-e308-4aeb-915f-12afd2adfa46.jpg")
                     screen.blit(image,(0,0))
                     pygame.display.update()
                     time.sleep(2)
                     mainCoordinateX = 250
                     mainCoordinateY = 250
            elif event.key==pygame.K_DOWN:
                if mainCoordinateY+20+25<500:
                 mainCoordinateY+=20
                else :
                     image=pygame.image.load(r"C:\Users\Dimash\Desktop\fd452307-e308-4aeb-915f-12afd2adfa46.jpg")
                     screen.blit(image,(0,0))
                     pygame.display.update()
                     time.sleep(5)
                     mainCoordinateX = 250
                     mainCoordinateY = 250
            elif event.key==pygame.K_LEFT:
             if mainCoordinateX-20-25>0:
                mainCoordinateX-=20
             else:
                 image = pygame.image.load(r"C:\Users\Dimash\Desktop\fd452307-e308-4aeb-915f-12afd2adfa46.jpg")
                 screen.blit(image, (0, 0))
                 pygame.display.update()
                 time.sleep(5)
                 mainCoordinateX = 250
                 mainCoordinateY = 250
            elif event.key==pygame.K_RIGHT:
             if mainCoordinateX+20+25<500:
                mainCoordinateX+=20
             else:
                 image = pygame.image.load(r"C:\Users\Dimash\Desktop\fd452307-e308-4aeb-915f-12afd2adfa46.jpg")
                 screen.blit(image, (0, 0))
                 pygame.display.update()
                 time.sleep(5)
                 mainCoordinateX = 250
                 mainCoordinateY = 250

pygame.quit()