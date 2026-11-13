
import pygame
import random
import board

image = pygame.image.load("borgir.png").convert_alpha()
image = pygame.transform.scale(image, (50, 50))


class FRUIT:
    def __init__(self, snake_positions):


        open_positions = []

        for row in range(board.ROWS):
            for col in range(board.COLS):

                position = (row, col)

                if position not in snake_positions:
                    open_positions.append(position)

        if open_positions:
            self.pos = random.choice(open_positions)
        else:
            self.pos = None

    def draw_fruit(self):

        if self.pos is None:
            return

        row, col = self.pos

        fruit_rect = pygame.Rect(
            col * board.SQUARE_SIZE,
            row * board.SQUARE_SIZE,
            board.SQUARE_SIZE,
            board.SQUARE_SIZE
        )

        board.screen.blit(image, fruit_rect)


fruit = None


            
