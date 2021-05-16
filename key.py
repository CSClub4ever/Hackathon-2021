# key.py
""" This file contains information about the win condition of the game """
from lib.graphics import Image

class Key:
    def __init__(self, pos, window):
        self.key = Image(pos, "src/assets/key.png")
        self.key.draw(window)

    def key_is_hit():
        """ This function would detect if the key is hit or not, if it has
        then the game would be won"""
        pass
