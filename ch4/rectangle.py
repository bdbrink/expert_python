
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        """rectangle width measured from left"""
        return self.x2 - self.x1
    
    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value
        
    @property
    def height(self):
        return self.y2 - self.y1
    
    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value

rectangle = Rectangle(10, 10, 25, 34)
print(f"the width is: {rectangle.width} \nthe width is: {rectangle.height}")