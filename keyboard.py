import pygame

pygame.init()

#variables 
width = 800
height = 800
x = width/2
y = height/2
x_change = 0
y_change = 0
speed = 0.5


screen = pygame.display.set_mode((width,height))

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)


#snake
snakeImg = pygame.image.load('snake 2.png')

def snake(x,y):
    screen.blit(snakeImg, (x,y))


running = True
while running:

    screen.fill((155,118,83))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # when keystroke is pressed, move by speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -speed
            if event.key == pygame.K_RIGHT:
                x_change = speed
            if event.key == pygame.K_UP:
                y_change = -speed
            if event.key == pygame.K_DOWN:
                y_change = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


    x += x_change
    y += y_change
    snake(x,y)
    pygame.display.update()