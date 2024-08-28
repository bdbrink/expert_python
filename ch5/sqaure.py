from dataclasses import dataclass

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

