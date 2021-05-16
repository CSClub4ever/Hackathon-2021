#SirVictoryGUI
from graphics import *

class GUI:
    def __init__(self):
        self.win = GraphWin("SirVictory- Urah rah", 1200, 700, autoflush=False)
        self.win.setCoords(0,0, 1200, 700)

        for i in range(0, 650, 100):
            r1 = Rectangle(Point(0, 50+i), Point(171, 100+i))
            r1.setFill("blue")
            r1.setOutline("blue")            
            r1.draw(self.win)

            r2 = Rectangle(Point(342, 50+i), Point(513, 100+i))
            r2.setFill("blue")
            r2.setOutline("blue")            
            r2.draw(self.win)

            r3 = Rectangle(Point(684, 50+i), Point(855, 100+i))
            r3.setFill("blue")
            r3.setOutline("blue")            
            r3.draw(self.win)

            r4 = Rectangle(Point(1026, 50+i), Point(1197, 100+i))
            r4.setFill("blue")
            r4.setOutline("blue")            
            r4.draw(self.win)

        self.time = Text(Point(1115, 675), "0")
        self.time.draw(self.win)
        self.instruction = Text(Point(600, 675), "Click to Begin Game")
        self.instruction.draw(self.win)
        self.record = Text(Point(85, 675), "0")
        self.record.draw(self.win)

        #update()
        self.win.getMouse()

    def close(self):
        self.win.close()

    def updateScore(self, score):
        self.score.setText(str(score))

    def updateTimer(self, time):
        self.time.setText(int(time))

if__name__=="__main__":
    from SirVictoryGame import Game
    gui = GUI()
    myGame = Game(gui)
    myGame.play()
        

            
