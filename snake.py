# backend
# stores coordinates of current snake
# moving of snake and adding blocks

class Snake:
    def __init__(self, x, y):
        self.head = [x, y]
        self.body = []

    def eat(self,f_x, f_y):
        self.body.append([f_x, f_y])

    def move_left(self):
        self.advance()
        self.head = [self.head[0] - 1, self.head[1]]

    def move_right(self):
        self.advance()
        self.head = [self.head[0] + 1, self.head[1]]

    def move_up(self):
        self.advance()
        self.head = [self.head[0], self.head[1] - 1]

    def move_down(self):
        self.advance()
        self.head = [self.head[0], self.head[1] + 1]
    
    def advance(self):
        self.body.insert(0, self.head)
        self.body.pop()

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.body[len(self.body) - 1]

    def get_body(self):
        return self.body
