# frontend game window
# takes care of controls and crash detection
import pygame
pygame.init()

numOfBlocks = 20 
block_width_height = 40
margin = 8  # space between the boxes
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
display = pygame.display.set_mode((numOfBlocks*block_width_height+(1+numOfBlocks)*margin,numOfBlocks*block_width_height+(1+numOfBlocks)*margin))

opened = True
while opened:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
       
    for column in range(numOfBlocks):
        x = margin + column * (block_width_height + margin)
        for row in range(numOfBlocks):
            y = margin + row * (block_width_height + margin) 
            rect = pygame.Rect(x, y, block_width_height, block_width_height)
            if(board[column][row] == 'b'):
                pygame.draw.rect(display, white, rect)
            if(board[column][row] == 's'):
                pygame.draw.rect(display, red, rect)
            if(board[column][row] == 'f'):
                pygame.draw.rect(display, blue, rect)
            
            

    pygame.display.update()