from tuple import *
from canvas import *

class Projectile:
    def __init__(self, position, velocity):
        self.position = position # point
        self.velocity = velocity # vector

class Environment:
    def __init__(self, gravity, wind):
        self.gravity = gravity   # vector
        self.wind = wind         # vector


# Progresses a projectile in an envoirment one unit of time
def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


if __name__ == "__main__":
    # Projectile starts one unit above orgin
    # Velocity is normalized to 1 unit/tick
    p = Projectile(point(0, 1, 0), normalize(vector(1, 1, 0)))

    # Gravity is -0.1 unit/tick, and wind is -0.01 unit/tick
    e = Environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

    tick_count = 0
    while p.position.y > 0:
        print("Tick {t}: ({x}, {y})".format(t=tick_count,
                                            x=p.position.x,
                                            y=p.position.y))
        p = tick(e, p)
        tick_count += 1

