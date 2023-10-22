from tuple import *
from canvas import *
from matrix import *

if __name__ == "__main__":
    # make a canvas (starts all black)
    c = Canvas(50, 50)
    # make a color to mark points with (say white)
    white = Color(1, 1, 1)
    # make a point at (0, 0, 1), or 12:00
    p = point(0, 0, 1)
    # make rotation matrix for later
    # represents a clockwise rotation around the y axis, pi/6 radians
    R = rotation_y(math.pi / 6)
    # 12 times:
    for i in range(12):
        # write white to point on canvas (p.x is x, and p.z is y)
        # converting the point coodinates to canvas indices goes like this:
        # canvas.x = p.x * {radius of clock in px} + {canvas.x at mid point}
        # canvas.y = p.z * {radius of clock in px} + {canvas.y at mid point}
        c.write_pixel(p.x * 15 + 25, p.z * 15 + 25, white)
        # rotate the point around the y axis pi/6 radians
        p = R * p
    # save canvas as an image
    c.to_image("./images/clock3.ppm")

