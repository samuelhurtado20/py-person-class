class Person:
    # Atributo de clase para almacenar instancias por nombre
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Agregamos la instancia actual al diccionario de la clase
        Person.people[name] = self

def create_person_list(people_dicts: list) -> list:
    # PASO 1: Crear todas las instancias primero
    # Esto asegura que todos los nombres existan en Person.people antes de vincularlos
    for p_dict in people_dicts:
        Person(p_dict["name"], p_dict["age"])

    # PASO 2: Crear la lista de retorno y establecer vínculos de matrimonio
    result = []
    for p_dict in people_dicts:
        person_instance = Person.people[p_dict["name"]]
        
        # Determinar si tiene 'wife' o 'husband' en el diccionario original
        partner_key = "wife" if "wife" in p_dict else "husband"
        partner_name = p_dict.get(partner_key)

        # Si hay un nombre de pareja, asignamos el objeto Person correspondiente como atributo
        if partner_name is not None:
            # Buscamos la instancia de la pareja en el diccionario de clase
            setattr(person_instance, partner_key, Person.people[partner_name])
        
        result.append(person_instance)
    
    return result
