# 🔹 Instance Variables vs Class Variables in Python
'''
✅ Instance Variables
    1. These are unique to each object (instance) of a class.
    2. Each time you create a new object, it gets its own separate copy of these variables.
    3. Changing one doesn't affect the other.

✅ Class Variables
    1. These are shared across all instances of the class.
    2. There is only one copy, and all objects refer to the same value unless overridden.
    3. But if you override it in one object, the new value will be available for that one object only.
    4. Remaining all objects will have the same value of Class Variable
    
✅ Python is more flexible and you don't need to declare instance variable in advance
    1. They are automatically created when the first time you assign them value using
        a. self.variable = value    # Inside a method
        b. 
'''
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)           # shared by all dogs # Output : 'canine'
print(e.kind)           # shared by all dogs # Output : 'canine'

print(d.name)           # unique to d        # Output : 'Fido'
print(e.name)           # unique to e        # Output : 'Buddy'

Dog.kind = 'doggo'      # This changes the shared class variable. 
#                       All instances that haven't overridden kind will now see 'doggo'.

print(d.kind)           # shared by all dogs # Output : 'doggo'
print(e.kind)           # shared by all dogs # Output : 'doggo'

d.kind = 'Burfi'        # Create an instance-level kind for d:
#                       Now d has its own kind, separate from the class.


print(d.kind)           # Now d has its own kind, separate from the class. # Output : 'Burfi'
print(e.kind)           # e still sees the class variable # Output : 'doggo'

Dog.kind = 'doggo'      # Change class variable again
print(d.kind)           # d now has its own kind, so this change does not affect it # Output : 'Burfi'
print(e.kind)           # e still refers to class variable → sees 'doggo' # Output : 'doggo'


#-------------------------------------------------------------------------------

class MyClass:
    school = 'ABC'
    
    def __init__(self, name):
        self.name = name
        
a = MyClass('Yogesh')

print(a.name)               # Output : Yogesh
print(a.school)             # Output : ABC
a.college = "RCPIT"     
print(a.college)            # Output : RCPIT

print(MyClass.school)       # Output : ABC
# print(MyClass.college)      # Output : AttributeError: type object 'MyClass' has no attribute 'college
MyClass.college = 'SSVP'    # Creating Class Variable at run time. not necessaryily declared in class definition
print(MyClass.college)      # Output : SSVP

MyClass.name = 'PQRS'       # Creating Class Variable at run time. not necessaryily declared in class definition
print(MyClass.name)         # Output : PQRS

# Conclusion : We can create instance as well as class variable at run time, without explicitly declaring them
# inside the class definition. Becuase Python is more flexible.

#-------------------------------------------------------------------------------
