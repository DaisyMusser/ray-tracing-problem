from color import *
from ppm import *

class Canvas():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.grid = [[Color(0, 0, 0) for x in range(w)] for y in range(h)]

    # Writes a color to a pixel on the grid
    # Rounds float x/ys to nearest whole numbers
    def write_pixel(self, x, y, color):
        x = round(x)
        y = round(y)
        self.grid[y][x] = color

    def read_pixel(self, x, y):
        return self.grid[y][x]

    def to_ppm(self):
        # Make a new ppm
        return Ppm(self)
        
        # Example string.format:
        # "P3\n{w} {h}\n255".format(w=canvas.width, h=canvas.height)

    # Creates an image file of this canvas
    # Will return error if filename already exists
    def to_image(self, fileName):
        f = open(fileName, "x")
        ppm = self.to_ppm()
        f.write(ppm.dump())
        f.close()
        # Bad practice
        print("Saved image to {name}".format(name=fileName))

    def is_on_grid(self, x, y):
        x = round(x)
        y = round(y)
        if x > self.width - 1:
            return False
        if y > self.height -1:
            return False
        return True
