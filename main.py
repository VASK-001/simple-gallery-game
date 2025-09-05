import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/trg3.png")
target_width = 70
target_height = 70

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = 1
while running:
    pass







pygame.quit()