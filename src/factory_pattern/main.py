from curses import KEY_RIGHT, window
from time import sleep
import pygame
import time


window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions)

x = 100
y = 100


pygame.init()
screen = pygame.display.set_mode((800, 600))

player_quits = False
while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))
    pygame.display.flip()
