from functools import singledispatch
from datetime import datetime

@singledispatch
def report(value):
    return f"raw: {value}"

def _(value: datetime):
    return f"dt: {value.isoformat()}"

print(report(12))

print(_(datetime.now))