# backend
# produces 2-d array according to the state of the game, snake, and food
# checks crash
from snake import Snake
import numpy as np
import random
class Game:

    def __init__(self, width, height):
        self.snake = Snake()
        self.width = width
        self.height = height

    def check_snake_crash():
        pass

    def move_up():
        pass

    def move_down():
        pass

    def move_right():
        pass

    def move_left():
        pass



    def eat():
        pass

    def place_new_food():
        pass

    def check_food_crach():
        pass



    def render():
        pass


    

if __name__ == "__main__" :
    random.seed(1)
    print(random.randint(1, 10))