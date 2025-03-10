import pygame
import random

# Pygame бастау
pygame.init()

# Экран өлшемдері
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Атыс ойыны")

# Түстер
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
blue = (50, 153, 213)
green = (0, 255, 0)

# Шрифт
font_style = pygame.font.SysFont("bahnschrift", 25)

# Ойыншының кемесі
player_width = 50
player_height = 50
player_x = width // 2
player_y = height - player_height - 10
player_velocity = 5

# Жау туралы деректер
enemy_width = 50
enemy_height = 50
enemy_velocity = 5

# Ойынның баллы
score = 0

# Ойыншының денесін салу
def draw_player(x, y):
    pygame.draw.rect(screen, green, [x, y, player_width, player_height])

# Жауды салу
def draw_enemy(x, y):
    pygame.draw.rect(screen, red, [x, y, enemy_width, enemy_height])

# Ойынның баллын шығару
def show_score(score):
    value = font_style.render(f"Ұпай: {score}", True, white)
    screen.blit(value, [10, 10])

# Ойынның басты функциясы
def gameLoop():
    global player_x, player_y, score

    game_over = False
    clock = pygame.time.Clock()

    # Жау құру
    enemy_list = []
    enemy_speed = 5
    def create_enemy():
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = -enemy_height
        enemy_list.append([enemy_x, enemy_y])

    # Ойынның логикасы
    while not game_over:
        screen.fill(black)

        # Ойындағы әрекеттер
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Ойыншы қозғалысы
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_velocity

        # Жау қозғалысы
        for enemy in enemy_list:
            enemy[1] += enemy_speed
            if enemy[1] > height:
                enemy_list.remove(enemy)
                score += 1

        # Жау мен ойыншының соқтығысуы
        for enemy in enemy_list:
            if player_x < enemy[0] + enemy_width and player_x + player_width > enemy[0]:
                if player_y < enemy[1] + enemy_height and player_y + player_height > enemy[1]:
                    game_over = True

        # Жауды және ойыншыны салу
        for enemy in enemy_list:
            draw_enemy(enemy[0], enemy[1])

        draw_player(player_x, player_y)
        show_score(score)

        # Жаңа жаулар жасау
        if random.random() < 0.03:  # 3% ықтималдықпен жаңа жау түсуі мүмкін
            create_enemy()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# Ойынды бастау
gameLoop()
