import pygame, random

pygame.init()
class Water(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.image=pygame.transform.scale(pygame.image.load(r"C:\Users\Dimash\Desktop\water.jpg").convert_alpha(),(200,200))
      self.image.set_colorkey((255,255,255))
      self.rect=self.image.get_rect()
      self.rect.topleft=(random.randint(100,500),0)
    def move(self):
        self.rect.y+=1
        if self.rect.y==800:
            self.rect.y=0
            self.rect.x=random.randint(100,500)
    def draw(self):
        screen.blit(self.image, self.rect)
class Drink(pygame.sprite.Sprite):

    def __init__(self, image_path, size=(150, 150), colorkey=(255, 255, 255)):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), size)
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(100, 500), 0)

    def move(self):

        self.rect.y+=1

        if self.rect.y==810:
            self.rect.y=0
            self.rect.x=random.randint(100,500)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Ranoldo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale(
            pygame.image.load(r"C:\Users\Dimash\Desktop\Cristiano-Ronaldo-Transparent-Background-PNG.png").convert_alpha(),(200,200)
        )
        self.image.set_colorkey((255,255,255))
        self.rect =self.image.get_rect()
        self.rect.topleft = (250, 650)

    def move(self):

        press=pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            self.rect.x-=1
        elif press[pygame.K_RIGHT]:
            self.rect.x+=1
    def draw(self,surface):
        surface.blit(self.image, self.rect)

screen = pygame.display.set_mode((578, 810))
cola = Drink(r"C:\Users\Dimash\Downloads\th__1_-removebg-preview.png")
Ranoldo7=Ranoldo()
sprite = Drink(r"C:\Users\Dimash\Downloads\th-removebg-preview.png" )
drinks = pygame.sprite.Group()
drinks.add(cola, sprite)
running = True
pygame.display.set_caption("AKZHOLEDU")
RANOLDO =pygame.sprite.Group()
RANOLDO.add(Ranoldo7)
waters=pygame.sprite.Group()
waters.add(Water())
fon = pygame.transform.scale(pygame.image.load(r"C:\Users\Dimash\Desktop\c626b01659dcbca44626f2c671f67f49.jpg"),
                             (578, 810))
count=0
font=pygame.font.SysFont("comicsans", 30)
pygame.mixer.music.load(r"C:\Users\Dimash\Downloads\NBSPLV - Lost Soul (Slowed).mp3")

pygame.mixer.music.play(-1)
while running:

    screen.blit(fon, (0, 0))
    RANOLDO.draw(screen)
    waters.draw(screen)
    drinks.draw(screen)
    for ranoldo in RANOLDO:
        ranoldo.move()
    for drink in drinks:
        drink.move()
    for water in waters:
        water.move()
    if pygame.sprite.spritecollideany(Ranoldo7,waters):
        count+=1

    gameOverText = font.render(f"Your score: {count}", True, (255, 0, 0))
    screen.blit(gameOverText, (10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()


