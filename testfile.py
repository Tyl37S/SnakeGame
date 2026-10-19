import pygame

# Initialize Pygame
pygame.init()

# Board settings
ROWS, COLS = 15, 15
SQUARE_SIZE = 50  # pixels per square
WIDTH, HEIGHT = COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE

# Colours
LIGHT = (114, 217, 111)  # light green
DARK = (111, 235, 92)    # dark green
PLAYER_COLOR = (255, 0, 0)

#start position
direction = (0, 1)

#movement delay
MOVEMENT_DELAY = 200  
last_move_time = pygame.time.get_ticks()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeBoard")
player_row, player_col = 0, 0

# Draw Snakeboard


# Main loop
def draw_player():
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        (player_col * SQUARE_SIZE, player_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    )

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (-1, 0)
            elif event.key == pygame.K_DOWN:
                direction = (1, 0)
            elif event.key == pygame.K_LEFT:
                direction = (0, -1)
            elif event.key == pygame.K_RIGHT:
                direction = (0, 1)
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVEMENT_DELAY:
        player_row += direction[0]
        player_col += direction[1]
        last_move_time = current_time

        # Stop if the player leaves the board
        if (player_row < 0 or player_row >= ROWS or
                player_col < 0 or player_col >= COLS):
            running = False

    draw_player()
    pygame.display.flip()

pygame.quit()


