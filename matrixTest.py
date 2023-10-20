import unittest
from matrix import *

class TestMatrixFeatures(unittest.TestCase):
    # Constructing and inspecting a 4x4 matrix
    def test_4x4_matrix(self):
        m = Matrix([[1,    2,    3,    4   ], 
                    [5.5,  5.6,  7.5,  8.5 ], 
                    [9,    10,   11,   12  ], 
                    [13.5, 14.5, 15.5, 16.5]])
        self.assertEqual(m.data[0][0], 1)
        self.assertEqual(m.data[0][3], 4)
        self.assertEqual(m.data[1][0], 5.5)
        self.assertEqual(m.data[1][2], 7.5)
        self.assertEqual(m.data[2][2], 11)
        self.assertEqual(m.data[3][0], 13.5)
        self.assertEqual(m.data[3][2], 15.5) 

    def test_2x2_matrix(self):
        m = Matrix([[-3,  5],
                    [ 1, -2]])
        self.assertEqual(m.data[0][0], -3)

    def test_3x3_matrix(self):
        m = Matrix([[-3,  5,  0],
                    [ 1, -2, -7],
                    [ 0,  1,  1]])
        self.assertEqual(m.data[0][0], -3)
        self.assertEqual(m.data[2][2], 1)

    def test_matrix_not_equals(self):
        a = Matrix([[0, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        b = Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        self.assertNotEqual(a.data, b.data)

    def test_matrix_equals(self):
        a = Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        b = Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        self.assertEqual(a.data, b.data)

    def test_matrix_epsilon_equals(self):
        a = Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        b = Matrix([[1, 2, 3, 4       ],
                    [5, 6, 7, 8       ],
                    [9, 8, 7, 6       ],
                    [5, 4, 3, 2.000001]])
        self.assertTrue(a.equals(b))

    def test_matrix_multipy(self):
        a = Matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
        b = Matrix([[-2, 1, 2,  3],
                    [ 3, 2, 1, -1],
                    [ 4, 3, 6,  5],
                    [ 1, 2, 7,  8]])
        c = Matrix([[20, 22, 50,  48 ],
                    [44, 54, 114, 108],
                    [40, 58, 110, 102],
                    [16, 26, 46,  42 ]])
        self.assertTrue((a * b).equals(c))

    def test_matrix_times_tuple(self):
        a = Matrix([[1, 2, 3, 4],
                    [2, 4, 4, 2],
                    [8, 6, 4, 1],
                    [0, 0, 0, 1]])
        b = Tuple(1, 2, 3, 1)
        self.assertTrue((a * b).equals(Tuple(18, 24, 33, 1)))

    def test_id_matrix(self):
        identity = Matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        m = Matrix([[1, 2, 3, 4],
                    [2, 4, 4, 2],
                    [8, 6, 4, 1],
                    [0, 0, 0, 1]])
        t = Tuple(1, 2, 3, 1)
        self.assertTrue((identity * m).equals(m))
        self.assertTrue((identity * t).equals(t))

    def test_transpose(self):
        a = Matrix([[0, 9, 3, 0],
                    [9, 8, 0, 8],
                    [1, 8, 5, 3],
                    [0, 0, 5, 8]])
        b = Matrix([[0, 9, 1, 0],
                    [9, 8, 8, 0],
                    [3, 0, 5, 5],
                    [0, 8, 3, 8]])
        self.assertTrue(a.transpose().equals(b))

    def test_id_transpose(self):
        identity = Matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        self.assertTrue(identity.transpose().equals(identity))
        
    def test_2x2_determinant(self):
        a = Matrix([[ 1, 5],
                    [-3, 2]])
        self.assertEqual(a.determinant(), 17)

    def test_submatrix_of_3x3(self):
        a = Matrix([[ 1, 5,  0],
                    [-3, 2,  7],
                    [ 0, 6, -3]])
        b = a.submatrix(0, 2)
        self.assertTrue(b.equals(Matrix([[-3, 2],
                                         [ 0, 6]])))

    def test_sub_4x4(self):
        a = Matrix([[0, 9, 3, 0],
                    [9, 8, 0, 8],
                    [1, 8, 5, 3],
                    [0, 0, 5, 8]])
        b = a.submatrix(1, 3)
        self.assertTrue(b.equals(Matrix([[0, 9, 3],
                                         [1, 8, 5],
                                         [0, 0, 5]])))

    def test_minor_3x3(self):
        a = Matrix([[3,  5,  0],
                    [2, -1, -7],
                    [6, -1,  5]])
        b = a.submatrix(1, 0)
        self.assertEqual(b.determinant(), 25)
        self.assertEqual(a.minor(1, 0), 25)

    def test_cofactor_3x3(self):
        a = Matrix([[3,  5,  0],
                    [2, -1, -7],
                    [6, -1,  5]])
        self.assertEqual(a.minor(0, 0), -12)
        self.assertEqual(a.cofactor(0, 0), -12)
        self.assertEqual(a.minor(1, 0), 25)
        self.assertEqual(a.cofactor(1, 0), -25)

    def test_determinant_3x3(self):
        a = Matrix([[ 1, 2,  6],
                    [-5, 8, -4],
                    [ 2, 6,  4]])
        self.assertEqual(a.cofactor(0, 0), 56)
        self.assertEqual(a.cofactor(0, 1), 12)
        self.assertEqual(a.cofactor(0, 2), -46)
        self.assertEqual(a.determinant(), -196)

    def test_determinant_4x4(self):
        a = Matrix([[-2, -8,  3,  5],
                    [-3,  1,  7,  3],
                    [ 1,  2, -9,  6],
                    [-6,  7,  7, -9]])
        self.assertEqual(a.cofactor(0, 0), 690)
        self.assertEqual(a.cofactor(0, 1), 447)
        self.assertEqual(a.cofactor(0, 2), 210)
        self.assertEqual(a.determinant(), -4071)

    def test_yes_invertible(self):
        a = Matrix([[6,  4, 4,  4],
                    [5,  5, 7,  6],
                    [4, -9, 3, -7],
                    [9,  1, 7, -6]])
        self.assertEqual(a.determinant(), -2120)
        self.assertTrue(a.is_invertible())

    def test_no_invertable(self):
        a = Matrix([[-4,  2, -2, -3],
                    [ 9,  6,  2,  6],
                    [ 0, -5,  1, -5],
                    [ 0,  0,  0,  0]])
        self.assertEqual(a.determinant(), 0)
        self.assertFalse(a.is_invertible())

    def test_inverse(self):
        a = Matrix([[-5,  2,  6, -8],
                    [ 1, -5,  1,  8],
                    [ 7,  7, -6, -7],
                    [ 1, -3,  7,  4]])
        b = a.inverse()
        self.assertEqual(a.determinant(), 532)
        self.assertEqual(a.cofactor(2, 3), -160)
        self.assertEqual(b.data[3][2], -160/532)
        self.assertEqual(a.cofactor(3, 2), 105)
        self.assertEqual(b.data[2][3], 105/532)
        self.assertTrue(b.equals(Matrix([[ 0.21805,  0.45113,  0.24060, -0.04511],
                                        [-0.80827, -1.45677, -0.44361,  0.52068],
                                        [-0.07895, -0.22368, -0.05263,  0.19737],
                                        [-0.52256, -0.81391, -0.30075,  0.30639]])))

    def test_product_times_inverse(self):
        a = Matrix([[-4,  2, -2, -3],
                    [ 9,  6,  8,  6],
                    [ 0, -5,  9, -5],
                    [ 0,  0,  4,  0]])
        b = Matrix([[-5,  2,  6, -8],
                    [ 1, -5, 10,  8],
                    [-7,  7, -6, -7],
                    [ 1, -3,  3,  4]])
        c = a * b
        self.assertTrue((c * b.inverse()).equals(a))

    def test_point_times_translation(self):
        trans = translation(5, -3, 2)
        p = point(-3, 4, 5)
        self.assertTrue((trans * p).equals(point(2, 1, 7)))

    def test_point_times_inversion(self):
        trans = translation(5, -3, 2)
        inv = trans.inverse()
        p = point(-3, 4, 5)
        self.assertTrue((inv * p).equals(point(-8, 7, 3)))

    def test_translating_vectors(self):
        trans = translation(5, -3, 2)
        v = vector(-3, 4, 5)
        self.assertTrue((trans * v).equals(v))
        
    def test_scaling_a_point(self):
        trans = scaling(2, 3, 4)
        p = point(-4, 6, 8)
        self.assertTrue((trans * p).equals(point(-8, 18, 32)))

    def test_scaling_a_vector(self):
        trans = scaling(2, 3, 4)
        v = vector(-4, 6, 8)
        self.assertTrue((trans * v).equals(vector(-8, 18, 32)))

    def test_inverse_scaling(self):
        trans = scaling(2, 3, 4)
        inv = trans.inverse()
        v = vector(-4, 6, 8)
        self.assertTrue((inv * v).equals(vector(-2, 2, 2)))

    def test_negative_scaling(self):
        trans = scaling(-1, 1, 1)
        p = point(2, 3, 4)
        self.assertTrue((trans * p).equals(point(-2, 3, 4)))

    def test_rotate_around_x(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(math.pi / 4)
        full_quarter = rotation_x(math.pi / 2)
        self.assertTrue((half_quarter * p).equals(point(0, math.sqrt(2)/2, math.sqrt(2)/2)))
        self.assertTrue((full_quarter * p).equals(point(0, 0, 1)))

    def test_inverse_rot_x(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(math.pi / 4)
        inv = half_quarter.inverse()
        self.assertTrue((inv * p).equals(point(0, math.sqrt(2)/2, -(math.sqrt(2)/2))))

    def test_rotate_around_y(self):
        p = point(0, 0, 1)
        half_quarter = rotation_y(math.pi / 4)
        full_quarter = rotation_y(math.pi / 2)
        self.assertTrue((half_quarter * p).equals(point(math.sqrt(2)/2, 0, math.sqrt(2)/2)))
        self.assertTrue((full_quarter * p).equals(point(1, 0, 0)))

    def test_rotate_around_z(self):
        p = point(0, 1, 0)
        half_quarter = rotation_z(math.pi / 4)
        full_quarter = rotation_z(math.pi / 2)
        self.assertTrue((half_quarter * p).equals(point(-(math.sqrt(2)/2), 
                                                           math.sqrt(2)/2,
                                                                        0)))
        self.assertTrue((full_quarter * p).equals(point(-1, 0, 0)))


if __name__ == "__main__":
    unittest.main()

