'''
What is a Class Method in Python?
--> A class method is a method that:
    1. Belongs to the class, not the instance
    2. Gets the class (cls) passed to it automatically instead of self

Why do we use @classmethod?
--> Sometimes, we want a method to:
    1. Work with class-level data
    2. Create objects in a special way
    3. Or do something that involves the class itself, not just an instance

How do you make a class method?
--> You use the @classmethod decorator or the classmethod() constructor.

What's really happening behind the scenes?
--> When you use @classmethod, Python:
    1. Wraps your function using the built-in classmethod() constructor
    2. This creates a class method object
    3. When called, this object automatically passes the class (cls) as the first argument

'''
class MyClass:
    @classmethod
    def show_class_name(cls):
        print("Class name is:", cls.__name__)

# Here:
# cls is automatically passed (just like self for regular methods)
# You can call this method using either the class or an instance

class Dog:
    species = "Canine"
    
    @classmethod
    def info(cls):
        return f"All dogs are {cls.species}"


print(Dog.info())  # "All dogs are Canine"

d = Dog()
print(d.info())  # still works, passes Dog as cls

# Summary:
# A class method is created using @classmethod (or classmethod()).
# It takes cls (the class) as the first argument instead of self.
# You can call it on the class itself or on an instance.
# Useful when you want to work with or modify class-level data.

# Quick Comparison Table :-
# ___________________________________________________________________________________________
# | Feature               | Instance Method   | Class Method         | Static Method        |
# | --------------------- | ----------------- | -------------------- | -------------------- |
# | Automatically gets    | self (instance)   | cls (class)          | Nothing              |
# | Access instance data? | ✅ Yes           | ❌ No                | ❌ No                |
# | Access class data?    | ✅ Yes           | ✅ Yes               | ❌ No                |
# | How to define         | def func(self)    | @classmethod         | @staticmethod        |
# | Common use            | Work with objects | Work with class/data | Utility/helper logic |
# |_______________________|___________________|______________________|______________________|


# Real World Use Case
'''
💡 Scenario: Managing an Employee Database
    We'll create an Employee class that uses:
    1. instance methods to show employee details
    2. a class method to create an employee from a string
    3. a static method to validate an email address
'''

import re

class Employee:
    company_name = "TechCorp"  # Class variable shared by all employees

    def __init__(self, name, age, email):
        self.name = name              # Instance variable
        self.age = age
        self.email = email

    # Instance method - works with instance variables
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Company: {Employee.company_name}")

    # Class method - used as an alternative constructor
    @classmethod
    def from_string(cls, emp_string):
        name, age, email = emp_string.split(",")
        return cls(name.strip(), int(age.strip()), email.strip())

    # Static method - utility function that doesn't depend on class or instance
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None


# Using the class

# Creating employees using regular constructor
emp1 = Employee("Alice", 30, "alice@techcorp.com")
emp2 = Employee("Bob", 28, "bob.techcorp.com")  # Invalid email

# Creating employee using class method
emp3 = Employee.from_string("Charlie, 25, charlie@techcorp.com")

# Using instance method
emp1.display_info()
emp3.display_info()

# Using static method for validation
print("Is emp1 email valid?", Employee.is_valid_email(emp1.email))  # True
print("Is emp2 email valid?", Employee.is_valid_email(emp2.email))  # False

# Changing class variable via class (affects all instances)
Employee.company_name = "NextGenSoft"

# Display info again to see updated company name
emp1.display_info()
emp3.display_info()


# 🧠 What This Shows:
# ________________________________________________________________________________________________________________
# | Method Type         | Usage in the Code       | Purpose                                                      |
# | ------------------- | ----------------------- | ------------------------------------------------------------ |
# | **Instance Method** | `display_info()`        | Access and display instance-level data                       |
# | **Class Method**    | `from_string()`         | Alternate constructor that creates an instance from a string |
# | **Static Method**   | `is_valid_email(email)` | A helper method that validates an email (no class data used) |
# |______________________________________________________________________________________________________________|

