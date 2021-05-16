#SirVictoryGame

from graphics import *
import time
class Game:
    def __init__(self, gui):
        self.gui = gui
        self.sirVictor = SirVictor(self.gui.win)
        self.sVmanager = SVmanager(self.gui.win)
        self.horns = Horns(self.gui.win)
        self.hornsList = []
        
    def play(self):
        fps = 50                 #Frames per second
        self.timeRemaining = 300 #total seconds in game
        self.record = 300         #default record

        while self.timeRemaining >0:
            self.SVmanager.moveSirVictory()
            self.checkKeyboard()
            for i in self.horns:
                i.move()
                if i.touch():
                    i.undraw()
                    self.horns.remove(i)
            self.hit3()
            self.timeRemaining = self.timeRemaining/fps
            self.gui.updateTimer(self.timeRemaining)

            update(fps)
        self.gui.close()

    def checkKeyboard(self):
        key = self.gui.win.checkKey()
        if key =="Left":
            self.SirVictor.moveLeft()
        elif key == "Right":
            self.SirVictor.moveRight()
        elif key == "q":
            self.gui.close()
        elif key == "space":
            self.SirVictor.jump()

if __name__ == "__main__":
    from SirVictoryGUI import GUI
    from sirVictor import SirVictor
    from sVmanager import SVmanager
    from horns import Horns


    gui = GUI()
    myGame = Game(gui)
    myGame.play()
        
            
        
        

        
        
        
