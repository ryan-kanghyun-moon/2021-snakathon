# backend
# stores coordinates of current snake
# moving of snake and adding blocks

class Snake:
    def __init__(self, x, y):
    
        self.body = [[x, y],[x, y + 1],[x, y + 2],[x, y + 3]]

    def eat(self,f_x, f_y):
        self.body.append([f_x, f_y])

    def move_left(self):
        head = self.body[0]
        new_head = [head[0] - 1, head[1]]
        self.body.insert(0,new_head)
        self.body.pop()
        
    def move_right(self):
        head = self.body[0]
        new_head = [head[0] + 1, head[1]]
        self.body.insert(0,new_head)
        self.body.pop()

    def move_up(self):
        head = self.body[0]
        new_head = [head[0], head[1] - 1]
        self.body.insert(0,new_head)
        self.body.pop()

    def move_down(self):
        head = self.body[0]
        new_head = [head[0], head[1] + 1]
        self.body.insert(0,new_head)
        self.body.pop()
    

    def get_head(self):
        return self.body[0]

    def get_tail(self):
        return self.body[len(self.body) - 1]

    def get_body(self):
        return self.body[1:]
