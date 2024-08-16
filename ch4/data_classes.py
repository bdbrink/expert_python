class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """add two vectors using + operator"""
        return Vector(
            self.x + other.y,
            self.y + other.y
        )
