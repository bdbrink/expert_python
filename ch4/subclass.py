from collections import UserDict
from typing import Any

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key: str, value: Any) -> None:
        return super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key: Any) -> Any:
        return super().__getitem__(key.lower())
    
    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())

d = CaseInsensitiveDict()

# Add items (case-insensitive)
d['Hello'] = 'World'
d['PyThOn'] = 'Programming'

print(d['hello'])
print(d['python'])

d['HELLO'] = 'Person'
print(d['Hello'])

# Delete an item
del d['PYthon']

# Check if a key exists
print('hello' in d)
print('python' in d)

# Get all items
print(d.items())