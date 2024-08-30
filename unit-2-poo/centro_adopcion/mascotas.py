class Pet():
    def __init__(self, id, name, birthdate, 
                register_date, specie, breed, 
                size, description, status):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.register_date = register_date
        self.specie = specie
        self.breed = breed
        self.size = size
        self.description = description
        self.status = status

    def show_info(self):
        print(self.name)

class Person():
    pass