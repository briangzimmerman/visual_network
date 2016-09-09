from Tkinter import *
from random import randint

class Ball:
    COLORS = {
        6: 'red',
        1: 'black',
        17: 'blue'
    }

    def __init__(self, canvas, protocol, data_size, max_x, max_y, direction):
        self.canvas = canvas
        self.start_y = randint(0, max_y)
        x = 0 if direction == 'INCOMING' else max_x - 15
        if protocol in self.COLORS:
            color = self.COLORS[protocol]
        else:
            color = 'orange'
        self.ball = canvas.create_oval(x, self.start_y, x+15, self.start_y+15, fill=color)
        self.max_y = max_y
        self.direction = direction
        self.move()

    def move(self):
        deltax = randint(0,5) if self.direction == 'INCOMING' else randint(-5, 0)
        deltay = randint(0,randint(1,5)) if self.start_y <= self.max_y / 2 else randint(randint(-5,-1),0)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move)
