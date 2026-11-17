import pygame, sys, random
from pygame.math import Vector2

import pygame
import sys
import board
import fruit
import snake
import audio


fruit.fruit = fruit.FRUIT(
    [(snake.player_row, snake.player_col)] + snake.snake_body)

pygame.init()
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(audio.music_file)
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





