import pygame
import numpy as np
import time
from game import Game
import sys

pygame.init()

numOfBlocks = 20 
block_width_height = 20
margin = 8  # space between the boxes
white = (255, 255, 255)
blues = (0, 0, 0)
display = pygame.display.set_mode((numOfBlocks*block_width_height+(1+numOfBlocks)*margin,numOfBlocks*block_width_height+(1+numOfBlocks)*margin+20))
game = Game(numOfBlocks, numOfBlocks)
board = game.render()
flag = "up"

snakeLength = 0

frame = 120
curr_frame = 0
opened = True
crashed = False
while opened:

    if crashed == True:
        while crashed:
            textFont = pygame.font.SysFont("comicsansms",20)
            score = 0 
            if snakeLength != 0: 
                score = snakeLength - 4
            textSurface = textFont.render("Crashed!. Press Space to restart. " + "final score: " + str(score), False, (0,200,0))
            # return textSurface, textSurface.get_rect()
            textRect = textSurface.get_rect()
            

            display.blit(textSurface, textRect)
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    opened = False
                    sys.exit()
                    

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        crashed = False
                        game = Game(numOfBlocks, numOfBlocks)
                        board = game.render()
                        flag = "up"
                        bb = pygame.Rect(0, 0, 500, 50)
                        pygame.draw.rect(display, (0, 0, 0), bb)
                        
            # return textSurface, textSurface.get_rect()
                        
       




    if game.did_snake_crash():
        crashed = True
        continue

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            opened = False
            continue

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board = game.move_left()
                flag = "left"
            if event.key == pygame.K_RIGHT:
                board = game.move_right()
                flag = "right"
            if event.key == pygame.K_UP:
                board = game.move_up()
                flag = "up"
            if event.key == pygame.K_DOWN:
                board = game.move_down()
                flag = "down"

    if (curr_frame == frame):
        if flag == "left":
            board = game.move_left()
        elif flag == "right":
            board = game.move_right()
        elif flag == "up":
            board = game.move_up()
        else:
            board = game.move_down()
    

    if board == False:
        crashed = True
        continue



    snakePosition = 0
    snakeLength = 0
    for x in range(numOfBlocks):
        for y in range(numOfBlocks):
            if(board[x][y] == 's'):
                snakeLength += 1

    rgbLength = (snakeLength - (snakeLength % 3))//3

    # for row in board:
    #     row.insert(0, 'w')
    #     row.append('w')
    # board.insert(0, ['w']*(numOfBlocks + 2))
    # board.append(['w']*(numOfBlocks + 2))

    for column in range(numOfBlocks):
        x = margin + column * (block_width_height + margin) 
        for row in range(numOfBlocks):
            y = margin + row * (block_width_height + margin) + 20
            rect = pygame.Rect(x, y, block_width_height, block_width_height)
            if(board[column][row] == 'b'):
                pygame.draw.rect(display, white, rect)
            if(board[column][row] == 's'):
                if(snakePosition < rgbLength):                
                    red = (255//rgbLength * (rgbLength - snakePosition))
                    green = (255//rgbLength * snakePosition)
                    blue = 0

                elif(snakePosition < (2  * rgbLength)):
                    red = 0
                    green = (255//(2* rgbLength)) * ((2 * rgbLength) - (snakePosition-1))
                    blue = (255//(2  * rgbLength)) * (snakePosition-1)

                else:
                    red = (255//snakeLength) * (snakePosition - 2)
                    green = 0
                    blue = (255//snakeLength) * (snakeLength - (snakePosition-2))

                pygame.draw.rect(display, (red, green, blue), rect)
                snakePosition += 1
            elif(board[column][row] == 'f'):
                pygame.draw.rect(display, blues, rect)
            elif(board[column][row] == 'w'):
                pygame.draw.rect(display, (0,0,0), rect)
            
   

    pygame.display.flip()
    # clock.tick(3)
    # time.sleep(0.3)
    curr_frame += 1
    curr_frame = curr_frame % (frame + 1)

    pygame.display.update()