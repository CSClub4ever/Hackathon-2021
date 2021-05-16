#sirVictor
from graphics import *

class SirVictor:
    def __init__(self,win):
        self.win = win
        self.step = 15
        
        for i in range(0, 51, 50):
            self.sirVictordown = Line(Point(400 + i, 675), Point(425 + i, 650))
            self.sirVictordown.draw(self.win)
            self.sirVictordown.setOutline("orange")

            self.sirVictorup = Line(Point(400 + i/2, 675), Point(425 + i/25, 650))
            self.sirVictorup.draw(self.win)
            self.sirVictorup.setOutline("orange")


    def moveLeft(self):
        self.sirVictor.move(-1*self.step, 0)

    def moveRight(self):
        self.sirVictor.move(self.step, 0)

    def jump(self):
        self.sirVictor.move(0, self.step)

    if __name__ == "__main__":
        from sirVictoryGUI import GUI
        from sirVictoryGame import Game
        gui = GUI()
        myGame = Game(gui)
        myGame.play()
