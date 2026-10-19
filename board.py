import pygame, random, sys

pygame.init()

# Colours
LIGHT = (114, 217, 111)  # light green
DARK = (111, 235, 92)    # dark green

# Board settings
ROWS, COLS = 15, 15
SQUARE_SIZE = 50  # pixels per square
WIDTH, HEIGHT = COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeBoard")

# Draw Snakeboard
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(screen,color,(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
