import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(v1 + v2)
    print(v1 * 3)

    print(abs(v1))
