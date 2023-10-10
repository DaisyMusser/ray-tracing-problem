import unittest
from tuple import *

# The test based on unittest module.
class TestTupleFeatures(unittest.TestCase):
    # tests a tuple with w = 1 is a point
    def test_point(self):
        a = Tuple(4.3, -4.2, 3.1, 1)
        self.assertEqual(a.x, 4.3, "incorrect x")
        self.assertEqual(a.y, -4.2, "incorrect y")
        self.assertEqual(a.z, 3.1, "incorrect z")
        self.assertEqual(a.w, 1, "incorrect w")
        self.assertTrue(a.isPoint(), "incorrect pointyness")
        self.assertFalse(a.isVector(), "incorrect vectorness")

    # tests a tuple with w = 0 is a vector
    def test_vector(self):
        a = Tuple(4.3, -4.2, 3.1, 0)
        self.assertEqual(a.x, 4.3, "incorrect x")
        self.assertEqual(a.y, -4.2, "incorrect y")
        self.assertEqual(a.z, 3.1, "incorrect z")
        self.assertEqual(a.w, 0, "incorrect w")
        self.assertFalse(a.isPoint(), "incorrect pointyness")
        self.assertTrue(a.isVector(), "incorrect vectorness")

    # tests point factory function
    def test_point_factory(self):
        p = point(4, -4, 3)
        self.assertTrue(p.equals(Tuple(4, -4, 3, 1)), "point didn't make a point")

    # tests vector factory function
    def test_vector_factory(self):
        v = vector(4, -4, 3)
        self.assertTrue(v.equals(Tuple(4, -4, 3, 0)), "vector didn't make a point")

    # tests if epsilon equals works
    def test_epsilon_equals(self):
        a = Tuple(1, 2, 3, 0)
        b = Tuple(1.000001, 2, 3, 0)
        c = Tuple(1.00001, 2, 3, 0)
        self.assertTrue(a.equals(b), "False not equal") 
        self.assertFalse(a.equals(c), "False equal")

    # Tests if tuple addition works.
    def test_tuple_add(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertTrue(a1.plus(a2).equals(Tuple(1, 1, 6, 1)), "Tuple addition broken.")

    # Tests subtracting two points
    def test_point_minus_point(self):
        p1 = point(3, 2, 1)
        p2 = point(5, 6, 7)
        self.assertTrue(p1.minus(p2).equals(vector(-2, -4, -6)), "point minus point broken")

    # Tests subtracting vector from point.
    def test_point_minus_vector(self):
        p = point(3, 2, 1)
        v = vector(5, 6, 7)
        self.assertTrue(p.minus(v).equals(point(-2, -4, -6)), "Point minus vector broken.")

    # Tests subtracting vector from vector. (change in direction between two vectors)
    def test_vector_minus_vector(self):
        v1 = vector(3, 2, 1)
        v2 = vector(5, 6, 7)
        self.assertTrue(v1.minus(v2).equals(vector(-2, -4, -6)), "Vector minus Vector broken.")
    
    # Tests zero vector minus another vector, or the negation of a vector.
    def test_negate_vector(self):
        zero = vector(0, 0, 0)
        v = vector(1, -2, 3)
        self.assertTrue(zero.minus(v).equals(vector(-1, 2, -3)), "Negate vector broken")

    # Test specific function for the above test.
    def test_negator(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue((-a).equals(Tuple(-1, 2, -3, 4)), "Negator function broken.")

    # Tests vector * scalar
    def test_vector_times_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue((a * 3.5).equals(Tuple(3.5, -7, 10.5, -14)), "Vector times scalar broken")

    # Tests vector * fraction
    def test_vector_times_fraction(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue((a * 0.5).equals(Tuple(0.5, -1, 1.5, -2)), "Vector times fraction broken")

    # Tests vector / scalar
    def test_vector_div_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue((a / 2).equals(Tuple(0.5, -1, 1.5, -2)), "Vector times fraction broken")

    # Tests the magnitude(vector) function
    def test_vector_magnitude(self):
        v = vector(1, 0, 0)
        self.assertEqual(magnitude(v), 1)
        v = vector(0, 1, 0)
        self.assertEqual(magnitude(v), 1)
        v = vector(0, 0, 1)
        self.assertEqual(magnitude(v), 1)
        v = vector(1, 2, 3)
        self.assertEqual(magnitude(v), math.sqrt(14))
        v = vector(-1, -2, -3)
        self.assertEqual(magnitude(v), math.sqrt(14))

    # Tests normalizing v(4 0 0)
    def test_vector_normalizing_400(self):
        v = vector(4, 0, 0)
        self.assertTrue(normalize(v).equals(vector(1, 0, 0)))

    # Tests normalizing v(1, 2, 3)
    def test_vector_normalizing_123(self):
        v = vector(1, 2, 3)
        self.assertTrue(normalize(v).equals(vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14))))

    # Tests that the magnitude of a normal vector is 1.
    def test_magnitude_of_normal_vector(self):
        v = vector(1, 2, 3)
        n = normalize(v)
        self.assertEqual(magnitude(n), 1)

    # Tests that dot product works.
    def test_dot_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(dot(a, b), 20)

    # Tests that cross product works.
    def test_cross_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertTrue(cross(a, b).equals(vector(-1, 2, -1)))
        self.assertTrue(cross(b, a).equals(vector(1, -2, 1)))


if __name__ == "__main__":
    # Run the test.
    unittest.main()
