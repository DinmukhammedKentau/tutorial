import pygame
import sys
from pygame.locals import *
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Racing Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game variables
speed = 5
score = 0
coins_collected = 0
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over_text = font.render('Game Over', True, BLACK)

# Load images
background = pygame.image.load(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8qaitalau\images\AnimatedStreet (2).png")
player_img = pygame.image.load(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8qaitalau\Player (2).png")
enemy_img = pygame.image.load(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8qaitalau\Enemy (2).png")
coin_img = pygame.image.load(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8qaitalau\images\coin (1).png")

# Load sounds
coin_sound = pygame.mixer.Sound(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8\Car\Sounds\coinsound.mp3")
crash_sound = pygame.mixer.Sound(r"C:\Users\Dimash\PycharmProjects\tutorial\Lab8\Car\Sounds\crash.wav")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.move_ip(5, 0)



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            score += 1
            self.rect.center = (random.randint(40, width - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(coin_img, (size, size))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > height:
            self.rect.center = (random.randint(40, width - 40), 0)

def get_user_name():
    name=""
    font=pygame.font.SysFont("comicsansms", 60)
    input_box=pygame.Rect(100,250,200,50)
    acrtive=False
    while True:
        screen.fill(WHITE)
        txt_surface=font.render(name,True,BLACK)

# Create sprites
player = Player()
enemy = Enemy()
coins = pygame.sprite.Group(
    Coin(15),
    Coin(25),
    Coin(35)
)

# Create sprite groups
all_sprites = pygame.sprite.Group(player, enemy, *coins)
enemies = pygame.sprite.Group(enemy)

# Speed increase timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == INC_SPEED:
            speed += 0.1

    # Draw background
    screen.blit(background, (0, 0))

    # Update and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Coin collision
    collected = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected:
        coins_collected += 1
        coin_sound.play()
        new_coin = Coin(coin.size)
        coins.add(new_coin)
        all_sprites.add(new_coin)

        if coins_collected % 4 == 0:
            speed += 0.2

    # Enemy collision
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        running = False

    # Display scores
    score_text = font_small.render(f'Score: {score}', True, BLACK)
    coins_text = font_small.render(f'Coins: {coins_collected}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (width - coins_text.get_width() - 10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()