

import time

import pygame
import board
import fruit
import sys
import random
import audio

growth_pending = 0

pygame.mixer.init()

face_image = pygame.image.load("smilyface.jpg").convert_alpha()
image = pygame.transform.scale(face_image, (50, 50))

# Starting position
direction = (0, 1)
player_row, player_col = 0, 0
MOVEMENT_DELAY = 170
KEY_DELAY = 0.017
HEAD_COLOR = (126, 126, 126)

last_move_time = pygame.time.get_ticks()
snake_body = []


def grow_snake():
    global growth_pending
    growth_pending += 1
    print("Snake is", len(snake_body) + growth_pending, "long")


def draw_player():
    # Draw the body
    if len(snake_body) < 15:
            PLAYER_COLOR = (0, 0, 126)
    elif len(snake_body) >= 15 and len(snake_body) < 30:
            PLAYER_COLOR = (134, 0, 0) 
    elif len(snake_body) >= 30:
            PLAYER_COLOR = (255, 215, 0)
    elif len(snake_body) == None:
            PLAYER_COLOR = (0, 0, 126)
            return PLAYER_COLOR
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
    board.screen.blit(image, (player_col * board.SQUARE_SIZE, player_row * board.SQUARE_SIZE))



def handle_key(event):
    global direction

    if event.key == pygame.K_UP and direction != (1, 0):
        time.sleep(KEY_DELAY)
        direction = (-1,0)
    elif event.key == pygame.K_DOWN and direction != (-1, 0):
        time.sleep(KEY_DELAY)
        direction = (1, 0)
        
    elif event.key == pygame.K_LEFT and direction != (0, 1):
        time.sleep(KEY_DELAY)
        direction = (0, -1)
    elif event.key == pygame.K_RIGHT and direction != (0, -1):
        time.sleep(KEY_DELAY)
        direction = (0, 1)
    elif event.key == pygame.K_LEFT and pygame.K_UP:
         time.sleep(KEY_DELAY)
         direction = (0, -1)
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

    eating = new_head == fruit.fruit.pos

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
        audio.sound.play()
        grow_snake()
        

        fruit.fruit = fruit.FRUIT([(player_row, player_col)] + snake_body)

    # Remove the tail unless growing
    if growth_pending > 0:
        growth_pending -= 1
    else:
        snake_body.pop()

    last_move_time = current_time


