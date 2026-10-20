

import time

import pygame
import board
import fruit
import sys
import random

pygame.mixer.init()
sound = pygame.mixer("chew.wav")
PLAYER_COLOR = (0, 0, 126)

# Starting position
direction = (0, 1)
player_row, player_col = 0, 0

MOVEMENT_DELAY = 200
last_move_time = pygame.time.get_ticks()

snake_body = []
growth_pending = 0

def grow_snake():
    global growth_pending
    growth_pending += 1
    print("Snake is", len(snake_body) + growth_pending, "long")


def draw_player():
    # Draw the body
    for row, col in snake_body:
        pygame.draw.rect(
            board.screen,
            PLAYER_COLOR,
            (
                col * board.SQUARE_SIZE,
                row * board.SQUARE_SIZE,
                board.SQUARE_SIZE,
                board.SQUARE_SIZE
            )
        )

    # Draw the head
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

#make a function that amkes the snake grow every time it eats a fruit


    




def update_player():
    global player_row, player_col, last_move_time, growth_pending

    current_time = pygame.time.get_ticks()

    if current_time - last_move_time < MOVEMENT_DELAY:
        return

    new_row = player_row + direction[0]
    new_col = player_col + direction[1]
    new_head = (new_row, new_col)

    # Die if the snake hits a wall
    if (new_row < 0 or new_row >= board.ROWS or
            new_col < 0 or new_col >= board.COLS):
        pygame.quit()
        sys.exit()

    # Check whether the snake eats the fruit
    eating = new_head == (
        int(fruit.fruit.pos.y),
        int(fruit.fruit.pos.x)
    )

    # The tail moves away unless the snake is growing
    if eating or growth_pending > 0:
        body_to_check = snake_body
    else:
        body_to_check = snake_body[:-1]

    # Die if the new head hits the body
    if new_head in body_to_check:
        print("GAME OVER! You hit yourself!")
        pygame.quit()
        sys.exit()

    # Save the old head position as a body segment
    snake_body.insert(0, (player_row, player_col))

    # Move the head
    player_row = new_row
    player_col = new_col

    # Grow when eating fruit
    if eating:
        grow_snake()
        sound.play()

        fruit.fruit = fruit.FRUIT()

    # Remove the tail unless growing
    if growth_pending > 0:
        growth_pending -= 1
    else:
        snake_body.pop()

    last_move_time = current_time


