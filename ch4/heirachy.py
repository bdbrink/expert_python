class CommonBase:
    pass

class Base1(CommonBase):
    pass

class Base2(CommonBase):
    def method(self):
        print("Base2.method() called")

class MyClass(Base1, Base2):
    pass

obj = MyClass()
obj.method()