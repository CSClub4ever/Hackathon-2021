# catapult.py
""" This file is in charge of the animation for the catapult firing """
from lib.graphics import Image, Point, update 

class Catapult:
    def __init__(self, window, location):
        self.window = window
        self.location = location
        self.catapult = Image(location, "src/assets/catapult0.png")
        self.catapult.draw(self.window)

    def launch(self):
        for i in range(6):
            new_image_path = "src/assets/catapult" + str(i) + ".png"
            self.catapult.undraw()
            self.catapult = Image(self.location, new_image_path)
            self.catapult.draw(self.window)
            
            

