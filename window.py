# frontend game window
# takes care of controls and crash detection
import pygame
import numpy as np
pygame.init()



numOfBlocks = 20 
block_width_height = 20
margin = 8  # space between the boxes
white = (255, 255, 255)
black = (0, 0, 0)
display = pygame.display.set_mode((numOfBlocks*block_width_height+(1+numOfBlocks)*margin,numOfBlocks*block_width_height+(1+numOfBlocks)*margin))
board = [['b','b','b','b','b','b','b','b','b','b'],['b','b','b','b','b','b','b','b','b','b'],['b','b','b','b','b','b','b','b','b','b'],['b','b','f','b','b','b','b','b','b','b'],['b','b','s','s','s','s','s','s','s','b'],['b','b','b','b','b','b','b','b','s','b'],['b','b','b','b','b','b','b','b','b','b'],['b','b','b','b','b','b','b','b','b','b'],['b','b','b','b','b','b','b','b','b','b'],['b','b','b','b','b','b','b','b','b','b']]

    
opened = True
while opened:
    snakePosition = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
    
    snakeLength = 0
    for x in range(numOfBlocks):
        for y in range(numOfBlocks):
            if(board[x][y] == 's'):
                snakeLength += 1

    
    


    rgbLength = (snakeLength - (snakeLength % 3))/3


        



    for column in range(numOfBlocks):
        x = margin + column * (block_width_height + margin)
        for row in range(numOfBlocks):
            y = margin + row * (block_width_height + margin) 
            rect = pygame.Rect(x, y, block_width_height, block_width_height)
            if(board[column][row] == 'b'):
                pygame.draw.rect(display, white, rect)
            if(board[column][row] == 's'):
                if(snakePosition < rgbLength):                
                    red = (255/rgbLength * (rgbLength - snakePosition))
                    green = (255/rgbLength * snakePosition)
                    blue = 0

                elif(snakePosition < (2  * rgbLength)):
                    red = 0
                    green = (255/(2* rgbLength)) * ((2 * rgbLength) - (snakePosition-1))
                    blue = (255/(2  * rgbLength)) * (snakePosition-1)

                else:
                    red = (255/snakeLength) * (snakePosition - 2)
                    green = 0
                    blue = (255/snakeLength) * (snakeLength - (snakePosition-2))

                pygame.draw.rect(display, (red,green,blue), rect)
                snakePosition += 1
            if(board[column][row] == 'f'):
                pygame.draw.rect(display, black, rect)
            
            

    pygame.display.update()