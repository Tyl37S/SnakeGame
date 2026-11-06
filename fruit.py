import pygame, sys, random
import board
import time
import snake

class FRUIT:
    def __init__(self):
        while True:
            self.x = random.randint(0,14)
            self.y = random.randint(0,14)
            self.pos = pygame.math.Vector2(self.x,self.y)
            if self.pos != (snake.player_row, snake.player_col) and self.pos not in snake.snake_body:
                break


    def draw_fruit(self):
        while self.pos == (snake.player_row, snake.player_col):
            self.pos = pygame.math.Vector2(random.randint(0,14),random.randint(0,14))
        
        fruit_rect = pygame.Rect(self.pos.x * board.SQUARE_SIZE,self.pos.y * board.SQUARE_SIZE,board.SQUARE_SIZE,board.SQUARE_SIZE)
        pygame.draw.rect(board.screen,(126,0,0),fruit_rect)
fruit = FRUIT()


            
