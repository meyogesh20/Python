'''
🔐 Private Variables - in Python there are no truly private variables
In Python, you can't really hide variables,
But there's a common rule that programmers follow: to tell others not to use them.

👉 If a variable starts with one underscore (like _age), it means: (protected variables by convention)
“This is private. Don't use it outside the class. it's for internal use only.”
It's not really hidden, but you should leave it alone because it might change without warning.

Sometimes, we want to hide things better — like when we don't want a child class to mess with
a variable in the parent class. For this, Python has a trick called name mangling:

👉 If a variable starts with two underscores (like __secret), Python changes its name behind the scenes
to something like _ClassName__secret. This makes it harder to access by accident, but it's still not 100% private.
This helps avoid problems if other parts of the code use the same name.

So, Python doesn't lock anything, but it gives you a way to keep things safe and clean in your code.
'''

class Person:
    def __init__(self, name, age):
        self.name = name            # Public variable
        self._age = age             # "Private" by convention
        self.__password = "secret"  # More private (name mangled)

# Create an object
p = Person("Alice", 30)

# You can access the public variable directly
print(p.name)         # Output: Alice

# You can still access _age, but it's a warning not to
print(p._age)         # Output: 30

# You cannot access __password directly
# print(p.__password) # ❌ This will cause an error

# But you can access it using its mangled name
print(p._Person__password)  # Output: secret


# 🔍 Summary:
# name: public – anyone can use it.

# _age: not really private, but "please don't touch it."

# __password: Python hides it a bit (renames it to _Person__password) so it's harder to mess with.