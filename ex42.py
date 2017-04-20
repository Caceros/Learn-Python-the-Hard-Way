class Animal():
    def __init__(self):
        print('Creating an Animal object')

class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.name = name

class Person():
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Fish():
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog('Rover')
print('Creating a Cat object')
satan = Cat('Satan')
mary = Person('Mary')
mary.pet = satan
frank = Employee('Frank', 120000)
frank.pet = rover
flipper = Fish()

