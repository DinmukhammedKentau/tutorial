import pygame
from datetime import datetime

pygame.init()
isDone = True
white = (255, 255, 255)
size = (450, 400)
screen = pygame.display.set_mode(size)
screen.fill(white)
clock = pygame.image.load("images/clock.png")
leftArmImage = pygame.image.load("images/leftarm.png")
rightArmImage = pygame.image.load("images/rightarm.png")
pygame.display.update()
leftArmAngle = 0
rightArmAngle = 0
print(datetime.now())
leftArmSecondImage=pygame.transform.scale(leftArmImage, (20, leftArmImage.get_height()//2.5-30))
rightArmHourImage=pygame.transform.scale(rightArmImage, (rightArmImage.get_width()//3,
                                                         rightArmImage.get_height()//3))
while isDone :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
    minute=datetime.now().minute
    second=datetime.now().second
    pygame.display.update()
    clock1=pygame.transform.scale(clock,(clock.get_width()//3,clock.get_height()//3))
    screen.blit(clock1,(0,0))

    leftArmAngle=(-6)*second
    rightArmAngle=(-6)*minute
    left=pygame.transform.rotate(leftArmSecondImage,leftArmAngle)
    leftImage=left.get_rect(center=(230,175))
    """центр деп типо ол тортбурышта журеди мики маустын колы 
    и соны айналдыру ушин оны тортбурышка катысты айналдырамыз"""

    """topleft деп жазамыз ойткени ол ози солай бекитилген сол жакка катысты айналдырамыз деп"""
    right=pygame.transform.rotate(rightArmHourImage,rightArmAngle)
    rightImage=right.get_rect(center=(230,175))
    screen.blit(left, leftImage.topleft)
    screen.blit(right,rightImage.topleft)
    pygame.display.flip()