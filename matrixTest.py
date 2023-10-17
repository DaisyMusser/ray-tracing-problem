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


if __name__ == "__main__":
    unittest.main()

