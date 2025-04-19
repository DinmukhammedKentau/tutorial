import pygame, random, time,sys
def checkCoordinate(enemy,coordinateOfCoin):
  if enemy.rect.left<coordinateOfCoin<enemy.rect.right:
      return False
  return True
black=(0,0,0)
pygame.mixer.init()
windowWidth = 400
windowHeight = 600
size = (windowWidth, windowHeight)
enemySpeed = 3
enemyCounter = 0
coinCounter = 0
playerSpeed = 3
blue=(0,0,255)
pygame.init()
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
red = (255, 0, 0)
screen.fill(white)
backgroungImage = pygame.image.load(r"../../Lab8qaitalau/images\AnimatedStreet (2).png")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../../Lab8qaitalau/Enemy (2).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(45, windowWidth - 45), 0)

    def move(self):
        global enemyCounter
        self.rect.move_ip(0, enemySpeed)
        if self.rect.top > windowHeight:
            enemyCounter += 1
            self.rect.bottom = 0
            self.rect.center = (random.randint(45, windowWidth - 45), 0)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../../Lab8qaitalau/Player (2).png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        isPressed = pygame.key.get_pressed()  # казир кандай клавиш басылганын тексеру
        if self.rect.top > 0:
            if isPressed[pygame.K_UP]:
                self.rect.move_ip(0, -playerSpeed)
        if self.rect.bottom < windowHeight:
            if isPressed[pygame.K_DOWN]:
                self.rect.move_ip(0, playerSpeed)
        if self.rect.left > 0:
            if isPressed[pygame.K_LEFT]:
                self.rect.move_ip(-playerSpeed, 0)
        if self.rect.right < windowWidth:
            if isPressed[pygame.K_RIGHT]:
                self.rect.move_ip(playerSpeed, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.transform.scale(pygame.image.load("../../Lab8qaitalau/images/coin (1).png"), (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(45, windowWidth - 45), 0)

    def move(self):
            global coinCounter
            self.rect.move_ip(0, enemySpeed)
            if self.rect.top > windowHeight:
                coinCounter -= 1
                coin.rect.center = (random.randint(30, windowWidth - 30), 0)


player = Player()
enemy = Enemy()
coin = Coin()

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

sprites = pygame.sprite.Group()
sprites.add(enemy)
sprites.add(coin)
sprites.add(player)

bigFont=pygame.font.SysFont("Times New Roman", 30)
smallFont=pygame.font.SysFont("Arial", 20)
gameOverText=bigFont.render("GAME OVER!!!", True,red)
isDone = True
newspeed=0.2+pygame.USEREVENT
pygame.mixer.music.load("Sounds/background.wav")
pygame.mixer.music.play(-1)
while (True):
    screen.blit(backgroungImage, (0, 0))
    enemyResultText=smallFont.render(f"Отип кеткен машиналар саны {enemyCounter}",True,blue)
    cointsResultText=bigFont.render(f"Сенин упайын {coinCounter}",True,blue)
    screen.blit(cointsResultText, (150, 10))
    screen.blit(enemyResultText, (150, 40))
    for sp in sprites:
        screen.blit(sp.image, sp.rect)
        sp.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
        if event.type==newspeed:
            enemySpeed+=2
    if pygame.sprite.spritecollideany(player, coins):
        coinCounter+=1
        pygame.mixer.Sound("Sounds/coinsound.mp3").play()

        coordinateOfCoin=random.randint(30, windowWidth - 30)
        coordinateOfEnemy=enemy.rect.center
        if checkCoordinate(enemy, coordinateOfCoin):
                coin.rect.center = (coordinateOfCoin, 0)
        else:
            if coordinateOfCoin +60< windowWidth:
                coin.rect.center=(coordinateOfCoin+60, 0)
            else :

                coin.rect.center=(coordinateOfCoin-60, 0)
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound("Sounds/crash.wav").play()
        time.sleep(2)
        screen.fill(black)
        screen.blit(gameOverText, (windowWidth//3,windowHeight//2))
        for sp in sprites:
            sp.kill()
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    pygame.display.update()
