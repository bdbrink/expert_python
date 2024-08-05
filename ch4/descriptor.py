class RevealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
        
    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val
    
    def __set__(self, obj, val):
        print("Updating", self.name)
        self.val = val
        
    def __delete__(self, obj):
        print("Deleting", self.name)
        del self.val
        
class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print(m.x)
m.x = 20
print(m.x)

def function(): pass
print(hasattr(function, '__get__'))
print(hasattr(function, '__set__'))