from tuple.py import *

class Projectile:
    def __init__(self, point, vector):
        self.position = point
        self.velocity = vector

class Environment:
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

def tick(env, proj):
    position = plus(proj.position, proj.velocity)
    velocity = plus(plus(proj.velocity, env.wind), env.gravity)
    return Projectile(position, velocity)
