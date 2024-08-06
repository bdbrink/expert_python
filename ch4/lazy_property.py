import OpenGL.GL as gl
from OpenGL.GL import shaders

class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function
        
    def __get__(self, obj, cls):
        value = self.fget(cls)
        
        setattr(cls, self.fget.__name__, value)
        return value