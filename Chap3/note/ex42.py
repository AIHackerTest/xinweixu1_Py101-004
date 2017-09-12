#Ex 42 is-a & has-a

## Animal is-a object
class Animal(object):
    pass

## the class "Dog" is-a "animal"
class Dog(Animal):
    # each instance of the class "Dog" has-a "name" attribute
    def __init__(self, name):
        # the "name" of each instance of "Dog" is defined by the variable "name"
        self.name = name

# the class "Cat" is-a "animal"
class Cat(Animal):
    # each instance of the class "Cat" has-a "name" attribute
    def __init__(self, name):
        self.name = name

# the class "Person" is-a "object":
class Person(object):
    # each instance of "Person" has-a "name" attribute
    def __init__(self, name):
        self.name = name
        # each instance of "Person" has-a pet of None
        self.pet = None

# the class "employee" is a "Person"
class Employee(Person):
    # each instance of "Employee" has-a "name" and "salary" attributes
    def __init__(self, name, salary):
        # the "name" of each instance of "Employee" is inherited from the "name" of the "Person"
        super(Employee, self).__init__(name)

        self.salary = salary

# the class "Fish" is-a object
class Fish(object):
    pass

# the class Salmon is-a Fish
class Salmon(Fish):
    pass

# the class Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")
# rover's "name" is "Rover"
print(rover.name)
# satan is-a Cat
satan = Cat("Satan")
# satan's name is "Satan"
print(satan.name)
# mary is-a "Person"
mary = Person("Mary")
# mary has-a pet satan
mary.pet = satan
print(mary.name)
print(mary.pet.name)

# frank is-a Employee
frank = Employee("Frank", 120000)
# frank has-a pet rover
frank.pet = rover
print(frank.salary)
print(frank.pet.name)

#flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
