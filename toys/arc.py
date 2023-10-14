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
    start = point(0, 1, 0)
    velocity = normalize(vector(1, 1.8, 0)) * 11.25
    p = Projectile(start, velocity)

    gravity = vector(0, -0.1, 0)
    wind = vector(-0.01, 0, 0)
    e = Environment(gravity, wind)

    red = Color(1, 0, 0)
    c = Canvas(900, 550)

    tick_count = 0
    while c.is_on_grid(p.position.x, p.position.y):
        print("Tick {t}: ({x}, {y})".format(t=tick_count,
                                            x=p.position.x,
                                            y=p.position.y))
        c.write_pixel(p.position.x, p.position.y, red)
        p = tick(e, p)
        tick_count += 1

    c.to_image("./images/arc.ppm")

