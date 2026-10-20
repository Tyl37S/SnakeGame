import pygame, sys, random
from pygame.math import Vector2

import pygame
import sys
import board
import fruit
import snake

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            snake.handle_key(event)

    snake.update_player()

    # Draw everything in order
    board.draw_board()
    fruit.fruit.draw_fruit()
    snake.draw_player()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()





