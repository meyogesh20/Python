# ✅ Class and Instance Variables
# Generally speaking, instance variables are for data unique to each instance and
# class variables are for attributes and methods shared by all instances of the class:

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

d.kind                  # shared by all dogs # Output : 'canine'
e.kind                  # shared by all dogs # Output : 'canine'

d.name                  # unique to d        # Output : 'Fido'
e.name                  # unique to e        # Output : 'Buddy'

