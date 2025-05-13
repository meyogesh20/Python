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

✅ Everything about the Class
1. Class definitions(class) like function definitions(def) must be executed before they have any effect.
    - This means that classes are create at runtime, not when the code is first read.
    - So you can't refer to a class before it has been created.
    - Also, since classes are created by executing their definition, you can define them inside
      conditions(if..elif) or functions like:
'''     
if True :
    class MyClass:
        pass
    
'''              
2. The statement inside a class definition will usually be function definitions,
   but other statements(ie. variable etc) are allowed. 
    - Below code prints something during class creation, not during object creation or use.
    
'''
print("before class defintion")                     # Output : before class defintion
class Demo:
    print("Hello, entered the class defintion")     # Output : Hello, entered the class defintion
    x = 42
    print("After delcaring class variable")         # Output : After delcaring class variable

print("After class defintion")                      # Output : After class defintion
a = Demo()      
print(a.x)                                          # Output : 42
a.x = 50

print(a.x)                                          # Output : 50

b = Demo()

# Conclusion : code executes line by line. print statements executed during class creation,
# not during the object creation and use. 

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
# Car.start(car1)  == car1.start()
# Car.start(car2)  exactly equivalent to car2.start()

'''
Method - is a function that belongs to an object.
In above code start() is a method.
Q - What exactly happens when a method is called? 
--> You may have noticed that car1.start() was called without an argument above,
even though the function definition for start() specified an argument. 

Q - What happened to the argument? 
Surely Python raises an exception when a function that requires an argument is called
without any — even if the argument isn't actually used…

💡 The special thing about methods is that the instance object is passed as the first argument
    of the function. In our example, the call car1.start() is exactly equivalent to Car.start(car1).
    1. self is just the name of the first argument, which Python fills in with the instance.
    2. car1.start() looks like a no-arg call, but car1 is passed automatically.
    3. You can even call the method manually with: Car.start(car1) 

In general, methods work as follows. 
1. Accessing a Method: When you do x.method, Python looks for method in the class of x.
2. Method Found: If method is a function in the class, Python creates a method object that
    remembers both the function and the instance x.
3. Calling the Method: When you call x.method(args), Python automatically passes x as the
    first argument (typically called self).
4. Behind the Scenes: 
    x.method(arg1, arg2) # is the same as: 
    ClassName.method(x, arg1, arg2)
5. Why It Matters: This lets the method know which object called it, so it can operate on that object's data.
'''
# Storing method for later
car3 = Car('US','Tesla') 
cs3 = car3.start       # Created method reference which belongs to car3 instance/object for later use
cs3()

cs1 = car1.start
cs2 = car2.start

print("create a list of functions reference to different objects")
functions = [cs1, cs2, cs3]
for func in functions:
    func()              # calling functions convenietly
    
# You can treat methods like values
# We can store method reference in list or other containers to use later.
