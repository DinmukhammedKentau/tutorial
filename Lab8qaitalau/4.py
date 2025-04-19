import time
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
enemy = pygame.image.load("Enemy (2).png")
running = True
player = pygame.image.load("Player (2).png")
player_x = random.randint(0, 800)
player_y = random.randint(0, 600)
enemy_x = random.randint(0, 800)
font = pygame.font.Font("freesansbold.ttf", 20)
clock = pygame.time.Clock()
enemy_y = random.randint(0, 600)

result = font.render("You did not win", True, (255, 255, 0))

while running:
    screen.fill((255, 255, 255))
    screen.blit(player, (player_x, player_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 1
    if keys[pygame.K_RIGHT]:
        player_x += 1
    if keys[pygame.K_UP]:
        player_y -= 1
    if keys[pygame.K_DOWN]:
        player_y += 1

    CorEnemy = random.randint(1, 2)
    if CorEnemy == 1:
        enemy_x = 5
        enemy_y -= 1
    elif CorEnemy == 2:
        enemy_x = -5
        enemy_y -= 1

    if enemy_y <= 0:
        enemy_y = 590
    if enemy_y >= 600:
        enemy_y = 0

    screen.blit(enemy, (enemy_x, enemy_y))

    player_rect = player.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

    # Егер ойыншы мен жау қақтығысса
    if player_rect.colliderect(enemy_rect):
        running = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Ойын аяқталған соң 2 секунд кідіріс қосу
if not running:
    screen.fill((255, 255, 255))
    screen.blit(result, (300, 250))  # Нәтижені экранда көрсету
    pygame.display.flip()
    time.sleep(2)  # 2 секунд кідіріс

    pygame.quit()
