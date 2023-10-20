from tuple import *
import copy

class Matrix:
    def __init__(self, data):
        self.data = data

    def equals(self, o):
        self_height  = len(self.data)
        self_width   = len(self.data[0])
        other_height = len(o.data)
        other_width  = len(o.data[0])
        if self_height == other_height:
            if self_width == other_width:
                for x in range(self_height):
                    for y in range(self_width):
                        if not epsilonEquals(self.data[x][y],
                                             o.data[x][y]):
                            return False
                return True
            else:
                return False
        else:
            return False

    def __mul__(self, x):
        if isinstance(x, Tuple):
            m = [None for x in range(4)]
            for row in range(4):
                m[row] = self.data[row][0] * x.x + self.data[row][1] * x.y + self.data[row][2] * x.z + self.data[row][3] * x.w
            return Tuple(m[0], m[1], m[2], m[3])
        else:
            m = [[None, None, None, None] for x in range(4)]
            for row in range(4):
                for col in range(4):
                    m[row][col] = self.data[row][0] * x.data[0][col] + self.data[row][1] * x.data[1][col] + self.data[row][2] * x.data[2][col] + self.data[row][3] * x.data[3][col]
            return Matrix(m)

    def transpose(self):
        t = [[None, None, None, None] for x in range(4)]
        for row in range(4):
            for col in range(4):
                t[col][row] = self.data[row][col]
        return Matrix(t)

    # A determinant is a weird number you can get from matrices. 
    # Idk how it works, google it...
    def determinant(self):
        m = self.data
        if len(m) == 2:
            det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        else:
            det = 0
            # Using row 0, but could be any row or col
            for col, num in enumerate(m[0]):
                det += num * self.cofactor(0, col)
        return det

    def submatrix(self, row, col):
        # not a deep copy!!
        sub = copy.deepcopy(self.data)
        # remove row
        sub.pop(row)
        for sub_row in sub:
            sub_row.pop(col)
        return Matrix(sub)

    # Shortcut for the determinant of the submatrix at row, col
    def minor(self, row, col):
        sub = self.submatrix(row, col)
        return sub.determinant()

    def cofactor(self, row, col):
        minor = self.minor(row, col)
        if (row + col) % 2 == 0:
            return minor
        else:
            return -minor

    def is_invertible(self):
        if self.determinant() == 0:
            return False
        else:
            return True

    def inverse(self):
        if not self.is_invertible():
            # throw error here??
            return False
        else:
            m = copy.deepcopy(self.data)
            for x, row in enumerate(m):
                for y, num in enumerate(row):
                    c = self.cofactor(x, y)
                    m[y][x] = c / self.determinant()
            return Matrix(m)


def translation(x, y, z):
    d = [[1, 0, 0, x],
         [0, 1, 0, y],
         [0, 0, 1, z],
         [0, 0, 0, 1]]
    return Matrix(d)

def scaling(x, y, z):
    d = [[x, 0, 0, 0],
         [0, y, 0, 0],
         [0, 0, z, 0],
         [0, 0, 0, 1]]
    return Matrix(d)

# Returns a matrix that will roate a point {angle} radians around x axis
def rotation_x(angle):
    d = [[1,               0,                0, 0],
         [0, math.cos(angle), -math.sin(angle), 0],
         [0, math.sin(angle),  math.cos(angle), 0],
         [0,               0,                0, 1]]
    return Matrix(d)

# Returns a matrix that will roate a point {angle} radians around y axis
def rotation_y(angle):
    d = [[ math.cos(angle), 0, math.sin(angle), 0],
         [               0, 1,               0, 0],
         [-math.sin(angle), 0, math.cos(angle), 0],
         [               0, 0,               0, 1]]
    return Matrix(d)

# Returns a matrix that will roate a point {angle} radians around z axis
def rotation_z(angle):
    d = [[math.cos(angle), -math.sin(angle), 0, 0],
         [math.sin(angle),  math.cos(angle), 0, 0],
         [              0,                0, 1, 0],
         [              0,                0, 0, 1]]
    return Matrix(d)

# Returns a matrix that will shear a point or vector
def shearing(xy, xz, yx, yz, zx, zy):
    d = [[ 1, xy, xz, 0],
         [yx,  1, yz, 0],
         [zx, zy,  1, 0],
         [ 0,  0,  0, 1]]  
    return Matrix(d)



