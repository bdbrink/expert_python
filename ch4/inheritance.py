class Base1:
    pass


class Base2:
    def method(self):
        print("Base2.method() called")

class MyClass(Base1, Base2):
    pass

obj = MyClass()
obj.method()