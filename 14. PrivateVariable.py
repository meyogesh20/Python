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


# ✅ Parent class
class Mapping:
    def __init__(self, iterable):
        self.items_list = []         # Public variable: can be accessed from outside
        self.__update(iterable)      # Call the private method (mangled to _Mapping__update)

    def update(self, iterable):
        # Public method: meant to add items to the list
        for item in iterable:
            self.items_list.append(item)

    __update = update                # Name-mangled private version of update()
    # Now __update is really _Mapping__update behind the scenes

# ✅ Subclass
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # This overrides the original update() method
        # Takes two arguments instead of one
        for item in zip(keys, values):
            self.items_list.append(item)
        # Even though update() is overridden, Mapping.__init__() still works
        # because it uses the private _Mapping__update


#✅ Final Output Behavior
# Test
m = Mapping([1, 2, 3])
print(m.items_list)  # [1, 2, 3]

ms = MappingSubclass([])
ms.update(['a', 'b'], [1, 2])
print(ms.items_list)  # [('a', 1), ('b', 2)]

# And notice: no errors from __init__ because it still uses the protected version of update().

'''           
✅ Explanation (Based on Variable Types):
1. self.items_list - Public Variable
    This is a normal public variable, accessible from outside the class.
    You can do obj.items_list without any issues.

2. self.__update() - Private Method via Name Mangling
    __update is a name-mangled version of the update() method.
    Python internally renames it to _Mapping__update.
    This protects it from being accidentally overridden in subclasses.

3. __update = update
    This line creates a private alias of the original update() method.
    So inside __init__(), even if a subclass overrides update(), 
        the original version is still safely called through __update().

4. update() is Overridden
    This method changes the update() method to accept two arguments, keys and values.
    However, __init__() in the parent class still works fine, because it doesn’t call
        this new method — it calls the private alias _Mapping__update.
        
🧩 Why This Matters
    This is a real use case for private variables:
🔐 It protects the original method from being overridden in subclasses,
    which could break functionality (like in __init__).
'''
