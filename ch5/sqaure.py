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
    