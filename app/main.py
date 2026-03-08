class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_dicts: list) -> list:
    for p_dict in people_dicts:
        Person(p_dict["name"], p_dict["age"])

    result = []
    for p_dict in people_dicts:
        person_instance = Person.people[p_dict["name"]]
        
        partner_key = "wife" if "wife" in p_dict else "husband"
        partner_name = p_dict.get(partner_key)

        if partner_name is not None:
            setattr(person_instance, partner_key, Person.people[partner_name])
        
        result.append(person_instance)
    
    return result
