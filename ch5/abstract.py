from abc import ABC, abstractmethod

class DummyInterface(ABC):
    
    @abstractmethod
    def dummy_method(self): ...
    
    @property
    @abstractmethod
    def dummy_property(self): ...