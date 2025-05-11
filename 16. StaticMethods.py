'''
🧠 What is a Static Method in Python?
    A static method is a method that belongs to the class rather than to any specific
    instance (object) of the class. It's a method that doesn't require access to the 
    instance (using self) or the class itself (using cls). Static methods are useful 
    for performing operations that don't need to modify the object or class state.

🔑 Key Characteristics of Static Methods:
    1.No Access to Instance (self) or Class (cls):
        A static method doesn't need access to the instance or class-level attributes or methods.
    2. It operates independently of the object it's called on. Callable via Class or Instance:
        You can call a static method on both the class and the instance.
    3. Unlike instance methods, static methods are not automatically passed the self or cls parameter.

Created Using staticmethod():
    Static methods are defined using the built-in staticmethod() function, 
        which wraps a function to make it a static method.

🔧 Why Use Static Methods?
    1. Encapsulation: Static methods allow you to keep related functions inside a class without
        needing to tie them to specific instances of the class.

    2. Utility Functions: They're often used for utility functions that are related to the class
        but don't need access to its state.

🧑‍🏫 Example: Defining and Using Static Methods
'''
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y


# Using Static Methods
print(MathUtils.add(5, 3))        # 8
print(MathUtils.subtract(10, 4))  # 6

'''
In the above example, add and subtract are static methods because they don't require access
to the instance (no self parameter) or the class (no cls parameter). 
They just perform a simple mathematical operation.

🧩 How Does staticmethod() Work?
    The staticmethod() function allows you to define a static method by "wrapping" a regular method inside
    a class without automatically passing the instance (self) or class (cls) as the first argument.

📄 What Happens Internally?
    A regular function is transformed into a static method using staticmethod().
    It’s a wrapper around the function, which means the function behaves the same way,
    but it’s now callable through the class or its instances.

'''
class Sample:
    @staticmethod
    def say_hello(name):
        print(f"Hello, {name}!")

# Get the static method object
hello_method = Sample.say_hello

# Call the static method directly via the object
hello_method("Alice")  # Output: Hello, Alice!

# Call the static method via the class
Sample.say_hello("Bob")  # Output: Hello, Bob!

'''
Here: hello_method is a static method object that we can call directly, bypassing the instance or the class.

🎯 Summary:
    1. A static method doesn't rely on the instance (self) or class (cls).
    2. It's a method that is bound to the class, not to the instance.
    3. Created using staticmethod(), it can be called on both the class and instances.
    4. It's useful for utility functions that don't modify the state of the class or its instances.
'''