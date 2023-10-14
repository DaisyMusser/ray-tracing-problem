from decimal import Decimal

EPSILON = 0.00001

# A Color is rgb tuple
class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    # Adds two colors. Overrides +
    def __add__(self, o):
        return Color(self.red + o.red,
                     self.green + o.green,
                     self.blue + o.blue)

    # Subtracts two colors. Overrides -
    def __sub__(self, o):
        return Color(self.red - o.red,
                     self.green - o.green,
                     self.blue - o.blue)

    # Multiplies a color by a scalar or another color. Overrides *
    def __mul__(self, o):
        if isinstance(o, Color):
            return Color(self.red * o.red,
                         self.green * o.green,
                         self.blue * o.blue)
        return Color(self.red * o,
                     self.green * o,
                     self.blue * o)

    # Checks if two colors are the same color.
    def equals(self, o):
        return epsilonEquals(self.red, o.red) and epsilonEquals(self.green, o.green) and epsilonEquals(self.blue, o.blue)

    # Returns string representing colors as "r g b"
    # Does the translating step: goes from 1 as max color value to 
    # whatever is passed in as max_color. Will clamp values < 0 or > 1.
    def toString(self, max_color):
        scaled_r = scale_color(self.red, max_color)
        scaled_g = scale_color(self.green, max_color)
        scaled_b = scale_color(self.blue, max_color)
        return "{r} {g} {b}".format(r=scaled_r, g=scaled_g, b=scaled_b)


# helper
def scale_color(c, max_color):
    if c < 0:
        return 0
    elif c > 1:
        return max_color
    elif c == 1:
        return max_color
    else:
        # Need the + 1 because 0 is always an option
        return Decimal(c * (max_color + 1))

# helper
def epsilonEquals(x, y):
    return abs(x - y) <= EPSILON

    
