import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка звуков
hit_sound = pygame.mixer.Sound("sound/hit.wav")  # попаданиe
miss_sound = pygame.mixer.Sound("sound/miss.wav")  # промах

target_img = pygame.image.load("img/trg3.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Перенесено внутрь цикла обработки событий
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hit_sound.play()  # Воспроизводим звук попадания
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                miss_sound.play()  # Воспроизводим звук промаха

    # Отрисовка
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))  # Исправлено: два аргумента вместо одного кортежа
    pygame.display.update()

pygame.quit()