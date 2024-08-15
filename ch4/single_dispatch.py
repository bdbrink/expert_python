from functools import singledispatch
from datetime import datetime
from numbers import Real

class Example:
    @singledispatch
    def method(self, arguement):
        pass
    
    @method.register
    def _(self, argument: float):
        pass

@singledispatch
def report(value):
    return f"raw: {value}"

@report.register
def _(value: datetime):
    return f"dt: {value.isoformat()}"

@report.register
def _(value: complex):
    return f"complex: {value.real}{value.imag:+}j"

@report.register
def _(value: Real):
    return f"real: {value:f}"

print(report(12))
report(datetime.now())