import pygame, sys

pygame.init()
screen = pygame.display.set_mode((750,750))
clock = pygame.time.Clock()
test_surface = pygame.Surface((200,200))
color = (100,155,0)
test_surface.fill((34,245,0))
x_pos = 200
while True:
    for event in pygame.event.get():
        if event.type  ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(color)
    screen.blit(test_surface,(x_pos,250))
    x_pos += 1
    pygame.display.update()
    clock.tick(60)