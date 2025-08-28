from typing import Any, Dict, List


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    """Create Person instances with relationships from dictionary data."""
    Person.people = {}

    person_list = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return person_list