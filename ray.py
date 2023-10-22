from tuple import *

class Ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t


class Sphere():
    def __init__(self):
        self.foo = "bar"


def intersect(sphere, ray):
    return []
