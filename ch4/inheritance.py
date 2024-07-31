class Base1:
    pass


class Base2:
    def method(self):
        print("Base2.method() called")

class MyClass(Base1, Base2):
    pass

obj = MyClass()
obj.method()

L[MyClass(Base1, Base2)] = [MyClass] + merge(L[Base1], L[Base2], [Base1, Base2])