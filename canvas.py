from color import *
from ppm import *

class Canvas():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.grid = [[Color(0, 0, 0) for x in range(w)] for y in range(h)]

    def write_pixel(self, x, y, color):
        self.grid[y][x] = color

    def read_pixel(self, x, y):
        return self.grid[y][x]

    def to_ppm(self):
        # Make a new ppm
        return Ppm(self)
        
        # Example string.format:
        # "P3\n{w} {h}\n255".format(w=canvas.width, h=canvas.height)
