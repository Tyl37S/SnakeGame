

import pygame
import board
import fruit
import sys
import random

PLAYER_COLOR = (0, 0, 126)

# Starting position
direction = (0, 1)
player_row, player_col = 0, 0

MOVEMENT_DELAY = 200
last_move_time = pygame.time.get_ticks()


def draw_player():
    pygame.draw.rect(
        board.screen,
        PLAYER_COLOR,
        (
            player_col * board.SQUARE_SIZE,
            player_row * board.SQUARE_SIZE,
            board.SQUARE_SIZE,
            board.SQUARE_SIZE
        )
    )


def handle_key(event):
    global direction

    if event.key == pygame.K_UP:
        direction = (-1, 0)
    elif event.key == pygame.K_DOWN:
        direction = (1, 0)
    elif event.key == pygame.K_LEFT:
        direction = (0, -1)
    elif event.key == pygame.K_RIGHT:
        direction = (0, 1)
def grow_snake():
    pygame.draw.rect(
        board.screen,
        PLAYER_COLOR,
        (player_col * board.SQUARE_SIZE ,
            player_row * board.SQUARE_SIZE,
            board.SQUARE_SIZE,
            board.SQUARE_SIZE)
    )

def update_player():
    global player_row, player_col, last_move_time

    current_time = pygame.time.get_ticks()

    if current_time - last_move_time >= MOVEMENT_DELAY:
        new_row = player_row + direction[0]
        new_col = player_col + direction[1]

        # Keep the player inside the board
        if (0 <= new_row < board.ROWS and
                0 <= new_col < board.COLS):
            player_row = new_row
            player_col = new_col

        last_move_time = current_time
#if the snake hits the walls it ends the game
        if (new_row < 0 or new_row >= board.ROWS or
            new_col < 0 or new_col >= board.COLS):
            pygame.quit()
            sys.exit()

        if (new_row, new_col) == (fruit.fruit.pos.y, fruit.fruit.pos.x):
            fruit.fruit = fruit.FRUIT() # Create a new fruit
            fruit.fruit.pos = pygame.Vector2(random.randint(0, board.COLS - 1), random.randint(0, board.ROWS - 1))
            grow_snake()  # Call the grow_snake function when the fruit is eaten
            

            last_move_time = current_time
