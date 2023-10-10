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


def epsilonEquals(x, y):
    return abs(x - y) <= EPSILON

    
