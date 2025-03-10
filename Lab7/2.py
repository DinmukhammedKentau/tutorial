import pygame
pygame.init()
screen = pygame.display.set_mode((1163, 535))
screen.fill('White')

isDone = True
index = 0
sounds = [
    r"C:\Users\Dimash\Downloads\MiyaGi & Эндшпиль - Fire Man.mp3",
    r"C:\Users\Dimash\Downloads\Виктор Цой - Группа крови.mp3",
    r"C:\Users\Dimash\Downloads\Miyagi - Captain.mp3"
]

isPaused = False
isPlayed = True
image=pygame.image.load(r"C:\Users\Dimash\Desktop\м.bmp")
while isDone:
    screen.blit(image, (0,0))
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            isDone = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if index == len(sounds) - 1:
                index = 0
            else:
                index += 1
            isPaused = False
            isPlayed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if index == 0:
                index = len(sounds) - 1
            else:
                index -= 1
            isPaused = False
            isPlayed = True

        if event.type == pygame.KEYDOWN  and isPlayed:
            if isPaused:
                pygame.mixer.music.unpause()
                isPaused = not isPaused
            else:
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play(2)
            isPlayed = not isPlayed

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed = not isPlayed
            isPaused = not isPaused

    pygame.display.flip()
