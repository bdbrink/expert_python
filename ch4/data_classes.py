from dataclasses import dataclass

@dataclass
class optimizedVector:
    x: int
    y: int
    
    def __add__(self, other):
        """add two vectors"""
        return optimizedVector(
            self.x + other.x,
            self.y + other.y,
        )
    
    def __sub__(self, other):
        """subtract two vectors using - operator"""
        return optimizedVector(
            self.x - other.x,
            self.y - other.y,
        )

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
    
    def __sub__(self, other):
        """subtract two vectors using - operator"""
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __repr__(self):
        """Return textual rep of vector"""
        return f"<Vector: x={self.x}, y={self.y}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

# Creating instances of optimizedVector
v1 = optimizedVector(3, 4)
v2 = optimizedVector(1, 2)

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

v1 = Vector(5, 7)
v2 = Vector(2, 3)

# Adding vectors
v3 = v1 + v2
print(v3)