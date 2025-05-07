'''✅  What is a Class? -->
1. A class is a blueprint for creating object and it groups state and behavior of object.
2. Objects are instances of classes. and they encapsulate data (attributes) and behavior (methods).
3. Python classes are flexible, dynamic, and follow OOP principles like encapsulation, inheritance, and polymorphism.
4. Python's approach is less strict and more dynamic than C++/Java, allowing rapid development.

✅ Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state.

Object Oriented Programming: 
1. The class inheritance mechanism allows **multiple base classes**
2. Derived class can override any methods of its base class or classes
3. A method can call the method of a base class with the same name. 
4. Objects can contain arbitrary amounts and kinds of data.

'''
# 1. Class Definition Syntax
class ClassName:                                # class keyword defines a new class.
    def __init__(self, attribute1, attribute2): # __init__ is the constructor method that initializes the object.
        self.attribute1 = attribute1            # Attributes are variables that store the state.
        self.attribute2 = attribute2

    def method_name(self):        # Methods are functions defined in the class that operate on its data.
        # logic here
        pass
    
# 💡 Key Concept: self
# self represents the instance of the class (like this in Java/C++).
# In Python, all instance methods must take self as their first parameter.
# self refers to the specific object the method is being called on.

class Car:
    def __init__(self, make, model):  # Constructor
        self.make = make              # Instance variable
        self.model = model

    def start(self):                 # Method
        print(f"{self.make} {self.model} is starting.")

car1 = Car('India','TATA Nexon')
car2 = Car('German','Mercedez Benz')

car1.start()    # Output : India TATA Nexon is starting.
car2.start()    # Output : German Mercedez Benz is starting.

# When you call a method like car1.start(), Python automatically passes the object car1 as the first argument.
