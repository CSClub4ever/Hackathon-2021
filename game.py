# game.py
""" The executable game file """
from cannonball import Cannonball
from catapult import Catapult
from key import Key

from lib.button import Button
from lib.graphics import *

class Game():

    def play(self):
        fps = 30
        self.window = GraphWin("Sir Victor's Quest", 1200, 800, autoflush=False)
        self.window.setCoords(0, 0, 1200, 800)
        self.window.setBackground("Light Blue")
        
        grass = Rectangle(Point(0, 0), Point(1200, 150))
        grass.setOutline("Green")
        grass.setFill("Green")
        grass.draw(self.window)
        
        key = Key(Point(800, 400), self.window)

        catapult = Catapult(self.window, Point(80, 193))
        self.window.getMouse()
        catapult.launch()
        
        self.c = Cannonball(self.window, Point(100, 200))
        self.c.launch(30, 45)
        self.window.getMouse()
        self.window.close()

if __name__=="__main__":
    game = Game()
    game.play()