from dataclasses import dataclass

@dataclass
class Person:
    age: int
    weight: int
    name: str

sorted(people, key=lambda person: person.age)
