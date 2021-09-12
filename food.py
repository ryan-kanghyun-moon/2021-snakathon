# backend
# keeps track of food 
import random
import time
import snake
class Food:
    def __init__(self, s_x, s_y):
        x = self.get_rand_int(-5 , 5)
        y = self.get_rand_int(-5 , 5)
        self.coord = [s_x + x, s_y + y]

    def place_new_food(self, snake, width, height):
        candidates = self.get_empty_coords(snake, width, height)
        self.coord = candidates[self.get_rand_int(0, len(candidates) - 1)]

    def get_empty_coords(self, snake, width, height):
        coords = [[]] * (width * height)

        for x in range(width):
            for y in range(height):
               coords[y * width + x] = [x, y] 

        for body in snake.get_body():
            coords.pop(body[1] * width + body[0])
        
        head = snake.get_head()
        coords.pop(head[1] * width + head[0])

        return coords


    def get_coord(self):
        return self.coord

    def get_rand_int(self, lo, hi):
        random.seed(round(time.time()) * 1000.0)
        return random.randint(lo, hi)