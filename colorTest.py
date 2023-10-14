import unittest
from color import *

class TestColorFeatures(unittest.TestCase):
    # Tests that colors are rgb tuples
    def test_colors(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)

    # Tests adding colors.
    def test_add_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertTrue((c1 + c2).equals(Color(1.6, 0.7, 1.0)))

    # Tests subtracting colors.
    def test_subtract_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertTrue((c1 - c2).equals(Color(0.2, 0.5, 0.5)))

    # Tests multiplying a color by a scalar.
    def test_times_scalar(self):
        c = Color(0.2, 0.3, 0.4)
        self.assertTrue((c * 2).equals(Color(0.4, 0.6, 0.8)))

    # Tests multiplying a color by a color.
    def test_color_times_color(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertTrue((c1 * c2).equals(Color(0.9, 0.2, 0.04)))


if __name__ == "__main__":
    unittest.main()
