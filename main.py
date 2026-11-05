import pygame, sys, random
from pygame.math import Vector2

import pygame
import sys
import board
import fruit
import snake

pygame.init()
pygame.init()
pygame.mixer.init()

import os

music_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Background2.mp3"
)

print("Mixer:", pygame.mixer.get_init())
print("Music file exists:", os.path.exists(music_file))

pygame.mixer.music.load(music_file)
pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.play(-1)
print("Music playing:", pygame.mixer.music.get_busy())


print("Background music started!")


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


pygame.mixer.music.stop()
pygame.quit()
sys.exit()





