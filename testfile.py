import pygame

# Initialize Pygame
pygame.init()

# Board settings
ROWS, COLS = 10, 10
SQUARE_SIZE = 50  # pixels per square
WIDTH, HEIGHT = COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE

# Colours
LIGHT = (114, 217, 111)  # light green
DARK = (111, 235, 92)    # dark green
PLAYER_COLOR = (255, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeBoard")
player_row, player_col = 0, 0

# Draw Snakeboard
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(
                screen,
                color,
                (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

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
            if event.key == pygame.K_UP and player_row > 0:
                player_row -= 1
            elif event.key == pygame.K_DOWN and player_row < ROWS - 1:
                player_row += 1
            elif event.key == pygame.K_LEFT and player_col > 0:
                player_col -= 1
            elif event.key == pygame.K_RIGHT and player_col < COLS - 1:
                player_col += 1

    draw_board()
    draw_player()
    pygame.display.flip()

pygame.quit()


