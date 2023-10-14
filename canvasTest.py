import unittest
from canvas import *

class TestCanvasFeatures(unittest.TestCase):
    # Creating a canvas
    def test_new_canvas(self):
        c = Canvas(10, 20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)
        for y in range(20):
            for x in range(10):
                self.assertTrue(c.grid[y][x].equals(Color(0, 0, 0)))

    # Writing pixels to a canvas
    def test_pixel_rw(self):
        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertTrue(c.read_pixel(2, 3).equals(red))

    # Constructing the PPM data
    def test_ppm_header(self):
        c = Canvas(5, 3)
        ppm = c.to_ppm()
        self.assertEqual(ppm.getHeader(), "P3\n5 3\n255\n")

    # Constructing the PPM pixel data
    def test_ppm_pixels(self):
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = c.to_ppm()
        self.assertEqual(ppm.getLines(3, 5), "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n")

    # Test we never exceed 70 char on a line
    # TODO: could be why you can't veiw an image!! (See page 22)

    # PPM files must end in \n
    def test_ppm_newline_terminated(self):
        c = Canvas(5, 3)
        ppm = c.to_ppm()
        self.assertEqual(ppm.dump()[-1], "\n")


if __name__ == "__main__":
    unittest.main()
