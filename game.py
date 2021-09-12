# backend
# produces 2-d array according to the state of the game, snake, and food
# checks crash
from snake import Snake
import numpy as np
import random
from food import Food
import time
class Game:

    def __init__(self, width, height):
        self.snake = Snake(width//2, height//2)
        self.food = Food(width//2, height//2)
        self.width = width
        self.height = height

    def did_snake_crash(self):
        head = self.snake.get_head()

        if head[0] < 0 or head[0] > self.width - 1 or head[1] < 0 or head[1] > self.height - 1:
            return True
        
        for body in self.snake.get_body():
            if body == head:
                return True
        
        
        return False

    def move_up(self):
        if not self.did_snake_crash():
            tail = self.snake.get_tail()
            self.snake.move_up()
        
            if self.is_food_edible():
                self.eat(tail)

        return self.render()
            

    def move_down(self):
        if not self.did_snake_crash():
            tail = self.snake.get_tail()
            self.snake.move_down()
        
            if self.is_food_edible():
                self.eat(tail)

            return self.render()
       

    def move_right(self):
        if not self.did_snake_crash():
            tail = self.snake.get_tail()
            self.snake.move_right()
        
            if self.is_food_edible():
                self.eat(tail)
            
            return self.render()
       

    def move_left(self):
        if not self.did_snake_crash():
            tail = self.snake.get_tail()
            self.snake.move_left()
        
            if self.is_food_edible():
                self.eat(tail)

            return self.render()
       



    def eat(self, tail):
        self.snake.eat(tail[0], tail[1])
        self.place_new_food()

    def place_new_food(self):
        self.food.place_new_food(self.snake, self.width, self.height)

    def is_food_edible(self):
        head = self.snake.get_head()
        return head == self.food.get_coord()



    def render(self):
        if self.did_snake_crash():
            return False

        board = [[]] * self.width
        for i in range(self.width):
            board[i - 1] = ['b'] * self.height
        
        for body in self.snake.get_body():
            board[body[0]][body[1]] = 's'
        
        head = self.snake.get_head()
        board[head[0]][head[1]] = 's'

        food = self.food.get_coord()
        board[food[0]][food[1]] = 'f'
       

        return board

    

