
## pythonic way for classes
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

obj = Point(1,2)

print(obj.x)
print(obj.y)
