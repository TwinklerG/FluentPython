from math import hypot

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # __abs__ is an inside function which can turn the absolute value of int or float
    # and can turn complex number into its modulus
    # hypot return the diagonal length of a right-angled triangle
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


print(Vector(2, 4) + Vector(2, 1))
print(abs(Vector(3, 4)))
print(Vector(3, 4) * 3)
print(abs(Vector(3, 4) * 3))