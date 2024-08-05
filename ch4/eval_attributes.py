import random

class InitOnAccess:
    def __init__(self, init_func, *args, **kwargs):
        self.klass = init_func
        self.args = args
        self.kwargs = kwargs
        self._initialized = None
        
    def __get__(self, instance, owner):
        if self._initialized is None:
            print("init!")
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print("cached!")
            return self._initialized

class WithSortedRandoms:
    lazy_init = InitOnAccess(sorted, [random.random() for _ in range(5)])

m = WithSortedRandoms()
print(m.lazy_init)