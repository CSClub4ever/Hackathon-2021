# cannonball.py
from lib.graphics import *
from math import sin, cos
from random import randrange
"""This file contains the mathematics surrounding the cannonball"""

class Cannonball:
    def __init__(self, window, start_loc):
        """contains the initialization of the cannonball object"""
        self.window = window
        self.cannonball = Circle(start_loc, 10)
        self.cannonball.setFill(color_rgb(255, 87, 34))
        self.cannonball.setOutline(color_rgb(255, 87, 34))
        self.cannonball.draw(self.window)

    def launch(self, velocity, launch_angle):
        """launches the cannonball from the catapult"""
        current_loc = self.cannonball.getCenter()
        t = 0

        while current_loc.getX() < 1200:
            current_loc = self.cannonball.getCenter()
            horiz_vel = velocity * cos(launch_angle)
            if current_loc.getY() > 150:
                vert_vel = velocity * sin(launch_angle) - t
            else:
                self.explode()
                break

            self.cannonball.move(horiz_vel, vert_vel)
            t += 1
            update()

    def explode(self):
        """ triggers cannonball's explosion animation """
        impact_pt = self.cannonball.getCenter()
        self.cannonball.undraw()
        r = randrange(0, 4)
        explosion_file = "src/assets/explosion" + str(r) + ".png"
        explosion = Image(impact_pt, explosion_file)
        explosion.draw(self.window)

        