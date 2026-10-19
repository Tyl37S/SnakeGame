import pygame, sys, random
import board
import time

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,14)
        self.y = random.randint(0,14)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * board.SQUARE_SIZE,self.pos.y * board.SQUARE_SIZE,board.SQUARE_SIZE,board.SQUARE_SIZE)
        pygame.draw.rect(board.screen,(126,0,0),fruit_rect)
fruit = FRUIT()


            




