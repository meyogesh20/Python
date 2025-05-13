'''
🔑 Key OOP Concepts -> 
4 core pillars of OOP:
    1. Encapsulation
    2. Inheritance
    3. Polymorphism
    4. Abstraction

🔒 1. Encapsulation — "Protecting the Data"
Idea: Encapsulation means hiding internal details of how an object works
    and protecting its data from outside interference.
    
💡 Why useful?
1. Keeps sensitive data secure
2. Only allows changes via defined methods

''' 
# 🔒 1. Encapsulation - Hiding Data Using Private Members

class BankAccount:
    # Constructor to initialize account owner and balance
    def __init__(self, owner, balance):
        self.owner = owner              # Public attribute
        self.__balance = balance        # Private attribute using double underscore (__)

    # Method to deposit amount into the account
    def deposit(self, amount):
        if amount > 0:                  # Ensure valid deposit
            self.__balance += amount    # Update private balance

    # Method to withdraw money from account
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:   # Check if enough balance
            self.__balance -= amount       # Deduct amount
        else:
            print("Insufficient funds.")   # Show error if withdrawal is not possible

    # Public method to access private balance
    def get_balance(self):
        return self.__balance              # Return current balance

# Usage
# Creating an account
acc = BankAccount("Alice", 1000)

# Depositing money
acc.deposit(500)

# Accessing balance via method
print(acc.get_balance())  # Output: 1500

# Trying to access private attribute directly (will raise error)
# print(acc.__balance)    # ❌ Error: AttributeError

'''
    
👪 2. Inheritance — "Reuse Code From a Parent"
Idea: Inheritance lets you create a new class from an existing class.
    The new class gets all the methods and attributes of the parent.
    
💡 Why useful?
1. Avoid code duplication
2. Share functionality across related classes
''' 
# 👪 2. Inheritance - Reusing Code from a Parent Class

# Base class
class Animal:
    # Constructor to initialize name
    def __init__(self, name):
        self.name = name

    # Base class method
    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class Dog inherits from Animal
class Dog(Animal):
    # Override the speak method
    def speak(self):
        print(f"{self.name} says Woof!")

# Derived class Cat inherits from Animal
class Cat(Animal):
    # Override the speak method
    def speak(self):
        print(f"{self.name} says Meow!")

# Usage

# Create Dog object
d = Dog("Buddy")
d.speak()  # Output: Buddy says Woof!

# Create Cat object
c = Cat("Whiskers")
c.speak()  # Output: Whiskers says Meow!


'''
🧬 3. Polymorphism — "Same Interface, Different Behavior"
Idea: Polymorphism means "many forms" — same method name behaves differently depending on the object.

💡 Why useful?
1. Enables flexible and extensible code
2. Supports interchangeable components
'''
# 🧬 3. Polymorphism - One Interface, Many Implementations

# Base class
class Bird:
    def fly(self):
        print("Some bird is flying")  # Base method

# Subclass Sparrow
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at low altitude")  # Custom behavior

# Subclass Eagle
class Eagle(Bird):
    def fly(self):
        print("Eagle flies at high altitude")   # Custom behavior

# A function that uses polymorphism
def let_it_fly(bird):
    bird.fly()  # Calls the appropriate fly() based on the object type

# Usage

# Test polymorphism
s = Sparrow()
e = Eagle()
b = Bird()

let_it_fly(s)  # Output: Sparrow flies at low altitude
let_it_fly(e)  # Output: Eagle flies at high altitude
let_it_fly(b)  # Output: Some bird is flying

'''
🧩 4. Abstraction — "Hiding Complex Details"
Idea: Abstraction means hiding complex logic and showing only the essential parts. It's like using 
    a TV remote you don’t know how it works internally, you just press buttons.
    
💡 Why useful?
1. Enforces a standard interface
2. Hides implementation details
3. Promotes consistency across different subclasses
''' 
# 🧩 4. Abstraction - Hiding Internal Logic via Interface

# Import abc module for abstract base classes
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    # Abstract method to be implemented by subclasses
    @abstractmethod
    def area(self):
        pass  # No implementation here

# Concrete class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # Area of circle

# Concrete class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Area of rectangle

# Usage :

# Create objects of concrete classes
c = Circle(5)
r = Rectangle(4, 6)

# Call area method - abstract interface, concrete logic
print(c.area())  # Output: 78.5
print(r.area())  # Output: 24

'''
🔁 Summary Table
___________________________________________________________________________________
| Concept       | Description                          | Keyword Used             |
| ------------- | ------------------------------------ | ------------------------ |
| Encapsulation | Hide internal data & control access  | `__private_var`          |
| Inheritance   | Reuse code from a parent class       | `class Child(Parent)`    |
| Polymorphism  | Same method name, different behavior | Method Overriding        |
| Abstraction   | Define template, hide inner logic    | `ABC`, `@abstractmethod` |
|_______________|______________________________________|__________________________|

'''
'''
🧠 Real-World Scenario: Employees in a Company
We'll model different types of employees (Developer, Manager) using:
Abstraction - Define what every employee must do (calculate_salary)
Inheritance - Share common properties from a base Employee class
Polymorphism - Let different employee types implement calculate_salary differently

'''

# Import necessary modules for abstraction
from abc import ABC, abstractmethod

# -------------------------------
# ABSTRACT BASE CLASS
# -------------------------------
class Employee(ABC):  # Abstract class defining the interface for all employees

    # Constructor to initialize name and base salary
    def __init__(self, name, base_salary):
        self.name = name                  # Public attribute for name
        self.base_salary = base_salary    # Public attribute for base salary

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def calculate_salary(self):
        pass  # No implementation here – forces subclasses to implement this method

    # Common method that all employees can use
    def get_details(self):
        return f"Employee Name: {self.name}"


# -------------------------------
# INHERITED SUBCLASS: Developer
# -------------------------------
class Developer(Employee):  # Inherits from Employee

    # Constructor includes name, base salary, and bonus
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # Call parent constructor
        self.bonus = bonus                   # Additional attribute for Developer

    # Implement the abstract method from Employee
    def calculate_salary(self):
        # Polymorphic behavior – specific to Developer
        return self.base_salary + self.bonus


# -------------------------------
# INHERITED SUBCLASS: Manager
# -------------------------------
class Manager(Employee):  # Inherits from Employee

    # Constructor includes name, base salary, and incentives
    def __init__(self, name, base_salary, incentives):
        super().__init__(name, base_salary)  # Call parent constructor
        self.incentives = incentives         # Additional attribute for Manager

    # Implement the abstract method from Employee
    def calculate_salary(self):
        # Polymorphic behavior – specific to Manager
        return self.base_salary + self.incentives


# -------------------------------
# POLYMORPHISM IN ACTION
# -------------------------------

# Function that accepts any employee and displays their salary
def display_salary(employee):
    # Call the calculate_salary method – actual behavior depends on object type
    print(f"{employee.get_details()} | Total Salary: ₹{employee.calculate_salary()}")


# -------------------------------
# TESTING ALL OOP CONCEPTS
# -------------------------------

# Create Developer object (using inheritance and abstraction)
dev = Developer("Alice", 70000, 10000)  # base salary + bonus

# Create Manager object (also uses inheritance and abstraction)
mgr = Manager("Bob", 90000, 15000)  # base salary + incentives

# Polymorphic behavior: same function works with different employee types
display_salary(dev)  # Calls Developer.calculate_salary
display_salary(mgr)  # Calls Manager.calculate_salary

# Output : 
# Employee Name: Alice | Total Salary: ₹80000
# Employee Name: Bob | Total Salary: ₹105000
