class RevealAccess(object):
    
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
        
    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
    
    def __set__(self, obj, val):
        print("Updating", self.name)
        self.val = val
        
    def __delete__(self, obj):
        print("Deleting", self.name)
        
class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print(m.x)