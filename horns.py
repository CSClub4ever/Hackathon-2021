#horns.py
from graphics import *
from random import choice
class Horns:
    def __init__(self, y, win):
        self.win = win
        if choice(["right_left", "left_right"]) == "right_left":
            self.velocity = -1
        else:
            self.velocity = 1
        self.y = y
        for i in range(0, 651, 150):
            self.lhorn = Polygon(Point(0, 113+i), Point(4, 100+i), Point(8, 104+i))
            self.rhorn = Polygon(Point(20,104+i), Point(24, 108+i), Point(28, 113+i))
            self.cap = Polygon(Point(4,100+i), Point(12,113+i), Point(24, 108))
            self.head = Polygon(Point(4,100), Point(12, 88), Point(24,108))
            self.H = [self.lhorn, self.rhorn, self.cap, self.head]
            self.H.setOutline("blue")
            self.H.draw(win)

    def move(self):
        self.H.move.
            
        
        
