import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ойынды бастау")

# Түстер
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 50)

# Батырма координаталары
play_button = pygame.Rect(300, 250, 200, 80)  # "Ойнау" батырмасы
exit_button = pygame.Rect(300, 350, 200, 80)  # "Шығу" батырмасы

# Суретті жүктеу
image = pygame.image.load(r"C:\Users\Dimash\Desktop\images (1).jpg")
x, y = 100, 100

game_started = False  # Ойын басталғанын тексеру

running = True
while running:
    screen.fill(YELLOW)

    if not game_started:
        # Ойынды бастау экраны
        pygame.draw.rect(screen, BLACK, play_button)
        pygame.draw.rect(screen, BLACK, exit_button)

        play_text = font.render("Ойнау", True, WHITE)
        exit_text = font.render("Шығу", True, WHITE)

        screen.blit(play_text, (play_button.x + 50, play_button.y + 20))
        screen.blit(exit_text, (exit_button.x + 50, exit_button.y + 20))

    else:
        # Ойын процесі
        screen.blit(image, (x, y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):  # "Ойнау" батырмасы
                    game_started = True
                elif exit_button.collidepoint(event.pos):  # "Шығу" батырмасы
                    running = False  # Ойынды жабу

        else:
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos  # Тышқанмен суретті жылжыту

pygame.quit()
