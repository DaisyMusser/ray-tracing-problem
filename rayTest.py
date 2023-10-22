import unittest
from ray import *

class TestRayFeatures(unittest.TestCase):
    def test_make_new_ray(self):
        origin = point(1, 2, 3)
        direction = vector(4, 5, 6)
        r = Ray(origin, direction)
        self.assertTrue(r.origin.equals(point(1, 2, 3)))
        self.assertTrue(r.direction.equals(vector(4, 5, 6)))

    def test_find_distance(self):
        r = Ray(point(2, 3, 4), vector(1, 0, 0))
        self.assertTrue(r.position(0).equals(point(2, 3, 4)))
        self.assertTrue(r.position(1).equals(point(3, 3, 4)))
        self.assertTrue(r.position(-1).equals(point(1, 3, 4)))
        self.assertTrue(r.position(2.5).equals(point(4.5, 3, 4)))

    def test_ray_intersecting_sphere_2x(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = intersect(s, r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0], 4.0)
        self.assertEqual(xs[1], 6.0)

    def test_tangent_ray_intersects_sphere(self):
        r = Ray(point(0, 1, -5), vector(0, 0, 1))
        s = Sphere()
        xs = intersect(s, r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0], 5.0)
        self.assertEqual(xs[1], 5.0)

    def test_ray_misses_sphere(self):
        r = Ray(point(0, 2, -5), vector(0, 0, 1))
        s = Sphere()
        xs = intersect(s, r)
        self.assertEqual(len(xs), 0)

    def test_ray_inside_sphere(self):
        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        s = Sphere()
        xs = intersect(s, r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0], -1.0)
        self.assertEqual(xs[1], 1.0)
    
    def test_sphere_behind_ray(self):
        r = Ray(point(0, 0, 5), vector(0, 0, 1))
        s = Sphere()
        xs = intersect(s, r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0], -6.0)
        self.assertEqual(xs[1], -4.0)
    

if __name__ == "__main__":
    unittest.main()

