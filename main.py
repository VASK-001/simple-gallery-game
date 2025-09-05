import pygame
import random
pygame.init()



target_img = pygame.image.load("img/trg3.png")
target_width = 70
target_height = 70

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = 1
while running:
    pass







pygame.quit()