import pygame, sys, random
from pygame.math import Vector2
import board
import fruit
pygame.init()
("SnakeBoard")
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
board.draw_board()
pygame.display.update()
pygame.display.set_caption("SnakeBoard")
pygame.display.flip()




