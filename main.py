import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        self.pos = pygame.math.Vector2(self.x,self.y *10)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y,cell_size,cell_size)
        pygame.draw.rect(screen,(126,0,0),fruit_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
color = (100,155,0)

fruit = FRUIT()


while True:
    for event in pygame.event.get():
        if event.type  ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)