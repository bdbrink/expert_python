from abc import ABC, abstractmethod
from dataclasses import dataclass

class DummyInterface(ABC):
    
    @abstractmethod
    def dummy_method(self): ...
    
    @property
    @abstractmethod
    def dummy_property(self): ...

class ColliderABC(ABC):
    @property
    @abstractmethod
    def bounding_box(self): ...
    
@dataclass
class Square(ColliderABC):
    ...

@dataclass
class Rect(ColliderABC):
    ...

@dataclass
class Circle(ColliderABC):
    ...

def find_collisions(objects):
    for item in objects:
        if not isinstance(item, ColliderABC):
            raise TypeError(f"{item} is not a collider")