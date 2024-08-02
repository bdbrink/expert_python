class RevealAccess(object):
    
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
        
    def __get__(self,obj, objtype):
        print("Retrieving", self.name)