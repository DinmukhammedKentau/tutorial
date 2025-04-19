import pygame,random
pygame.init()
tusu=0
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Catch the falling objects")
clock=pygame.time.Clock()
tus = random.randint(0, 255)
running=True
razmer = random.randint(10, 100)
counter=0
circle_x=400
enemy_x = random.randint(0, 800)
while running:
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("comicsans", 30)
    result=font.render(f"YOUR POINT:{counter}",True,(255,0,0))
    screen.blit(result, (400, 300))

    tusu+=1
    enemy = pygame.draw.rect(screen, (tus,tus,tus), (enemy_x, tusu, razmer, razmer))

    circle = pygame.draw.circle(screen, (255, 0, 0), (circle_x, 600), 50)
    if tusu==550:
        tusu=0

        razmer = random.randint(10, 100)
        tus=random.randint(0, 255)
        enemy_x = random.randint(0, 800)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                circle_x+=50
            elif event.key==pygame.K_LEFT:
                circle_x-=50
    circle_rect=pygame.Rect(circle_x-50,600-50,100,100)
    enemy_rect=pygame.Rect(enemy_x,tusu,razmer,razmer)
    if circle_rect.colliderect(enemy_rect):
      counter+=1
      tusu=0
      razmer = random.randint(10, 100)
      tus = random.randint(0, 255)
      enemy_x = random.randint(0, 800)
    pygame.display.flip()
