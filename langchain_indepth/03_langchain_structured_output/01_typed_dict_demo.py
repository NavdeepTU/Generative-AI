from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {"name": "navdeep", "age": 25}

print(new_person)

# {'name': 'navdeep', 'age': 25}