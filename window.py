import pygame
pygame.init()

display = pygame.display.set_mode((932,932))
block_width_height = 80
margin = 8  # space between the boxes
white = (255, 255, 255)

opened = True
while opened:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
            
    for column in range(20):
        x = margin + column * (block_width_height + margin)
        for row in range(20):
            y = margin + row * (block_width_height + margin) 
            rect = pygame.Rect(x, y, block_width_height, block_width_height)
            pygame.draw.rect(display, white, rect)

    pygame.display.update()