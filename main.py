import pygame, sys, random
from pygame.math import Vector2
import board
import fruit
import snake
pygame.init()
("SnakeBoard")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    board.draw_board()
    fruit.fruit.draw_fruit()
    snake.draw_player()
    pygame.display.set_caption("SnakeBoard")
    pygame.display.update()




