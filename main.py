import pygame, sys, random
from pygame.math import Vector2

import pygame
import sys
import board
import fruit
import snake

pygame.init()
pygame.mixer.init()

music_file = "Background2.mp3"
pygame.mixer.music.load(music_file)
pygame.mixer.music.set_volume(1)
  # repeat when the music ends

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
    pygame.mixer.music.play()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()


    pygame.display.flip()
    clock.tick(60)


pygame.mixer.music.stop()
pygame.quit()
sys.exit()





