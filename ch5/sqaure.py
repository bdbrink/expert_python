from dataclasses import dataclass
import itertools

@dataclass
class Sqaure:
    x: float
    y: float
    size: float
    
    @property
    def bounding_box(self):
        return Box(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size
        )

@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float
    
    @property
    def bounding_box(self):
        return Box(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height
        )

@dataclass
class Circle:
    x: float
    y: float
    radius: float
    
    @property
    def bounding_box(self):
        return Box(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )

@dataclass
class Box:
    x1: float
    y1: float
    x2: float
    y2: float

def find_collisions(objects):
    return [
        (item1, item2)
        for item1, item2
        in itertools.combinations(objects, 2)
        if rects_collide(
            item1.bounding_box,
            item2.bounding_box
        )
    ]

for collision in find_collisions([
    Sqaure(0,0,10),
    Rect(5,5,20,20),
    Sqaure(15,20,5),
    Circle(1,1,2)
]):
    print(collision)