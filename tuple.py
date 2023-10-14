import math

# The minimuim difference between two values we will still pretend are equal.
# Because of weird floating point math, with e = .00001, 0 == .000001 but 0 /= .00001
EPSILON = 0.00001

# My tuple class. Tuples represent points or vectors
class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    # check if object is a point
    def isPoint(self):
        return self.w == 1

    # check if object is a vector
    def isVector(self):
        return self.w == 0

    # for tuples to be the same they must have all the same values. Can be different objects.
    def equals(self, o):
        return epsilonEquals(self.x, o.x) and epsilonEquals(self.y, o.y) and epsilonEquals(self.z, o.z) and epsilonEquals(self.w, o.w)

    # Adds two tuples. Can add vector to a point, vector to a vector, but not point to point (will give tuple that is neither vector nor point.
    def __add__(self, o):
        return Tuple(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)
    
    # Subtracts tuples. Point - point gets a vector pointing from one to the other, point - vector gets a point.
    def __sub__(self, o):
        return Tuple(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    # (-a) Subtracts self from the zero vector to negate a vector. Calling on a point returns nonsense.
    def __neg__(self):
        zero = Tuple(0, 0, 0, 0)
        return zero - self

    # (a * x) vector times scalar/fraction.
    def __mul__(self, x):
        return Tuple(self.x * x, self.y * x, self.z * x, self.w *x)

    # a / x
    def __truediv__(self, x):
        return Tuple(self.x / x, self.y / x, self.z / x, self.w / x)



# Helper determines if two values are within epsilon of eachtother
def epsilonEquals(x, y):
    return abs(x - y) <= EPSILON

# Factory function for making tuples
# Makes a point
def point(x, y, z):
    return Tuple(x, y, z, 1)

# Makes a vector
def vector(x, y, z):
    return Tuple(x, y, z, 0)

# Gets the magnitude of a vector.
def magnitude(v):
    return math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)

# Normalizes a vector. 
# Reduces magnitude to 1 while perseving the same direction.
def normalize(v):
    m = magnitude(v)
    return Tuple(v.x / m,
                 v.y / m,
                 v.z / m,
                 v.w / m)

# Takes the dot product of a vector.
# This is the sum of the products of each component of two vectors.
def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w + b.w

# Gives the cross product of two vectors:
# the vector perpendicular to the two vectors given.
def cross(a, b):
    return vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)

