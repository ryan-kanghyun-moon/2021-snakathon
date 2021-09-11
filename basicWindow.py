import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width,height))

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)


# Game Loop
running = True
while running:
    for closeTap in pygame.event.get():
        if closeTap.type == pygame.QUIT:
            running = False

    # RGB - Red, Green, Blue
    screen.fill((155, 118, 83))
    pygame.display.update()