'''
🧠 What Are Getters and Setters?
    In many object-oriented programming languages, getters and setters are methods used to access (get) 
    or update (set) the value of an object's attributes. This is useful because it allows you to control
    how the data is accessed or modified.
    
    In Python, however, we often avoid explicit getter and setter methods for simplicity. Instead,
    Python provides a clean and powerful way to achieve this with the @property decorator and the 
    @<property_name>.setterdecorator.
   
🏠 The @property Decorator
    The @property decorator in Python allows you to define a method that acts like an attribute. 
    This method is automatically called when the attribute is accessed, but it looks and behaves 
    like a simple variable.

Why Use @property?
    1. You might want to compute or transform the value of an attribute dynamically when it's accessed.
    2. You want to add validation or logic when getting the value.
    3. You don't want users to directly access internal attributes but still need to expose them safely.
     
'''
class Rectangle:
    def __init__(self, width, height):
        self._width = width  # private variable
        self._height = height  # private variable

    @property
    def area(self):
        return self._width * self._height

# We use @property to define a method area that calculates the area of the rectangle.
# We don't store the area directly; it's computed on the fly whenever we access area.

rect = Rectangle(5, 3)
print(rect.area)  # This calls the 'area' method behind the scenes, output: 15

# Notice that when we access rect.area, it looks like we’re accessing an attribute,
# but behind the scenes, it's calling the area() method.

'''
🛠 The @<property_name>.setter Decorator
    Now that we have a getter using @property, we might want to control how we set an attribute. 
    For example, we might want to add a validation check when setting an attribute value.
        To define a setter for a property, we use the @<property_name>.setter decorator. It allows us 
        to control what happens when we set the value of an attribute.

Example: Using @property with a Setter
    Let's enhance the Rectangle class by adding validation to ensure that the width and height are 
    always positive values.
'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive!")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive!")
        self._height = value
# Here:
# 1. We have a getter width and height that simply return the values of _width and _height.
# 2. We’ve added a setter for width and height that ensures the values are positive. If someone
#    tries to set a negative value, it raises an error.

rect = Rectangle(5, 3)
print(rect.width)  # 5
print(rect.height)  # 3

# Now, let's try to set a negative value for width
rect.width = -2  # This will raise a ValueError

# When you try to set rect.width = -2, Python will call the setter and raise
# a ValueError because the value is invalid.

'''
💡 Why Use @property and @setter?
    1. Encapsulation: You can control how data is accessed or modified without exposing the underlying 
        implementation details.
    2. Validation: You can easily add logic for validation or transformation when getting or setting an attribute.
    3. Cleaner Code: You don’t have to create traditional getter and setter methods like in other languages. 
        You can directly use a method that behaves like an attribute, keeping the code clean and readable.

🎯 Recap:
@property: Turns a method into a "getter" that behaves like an attribute. Useful for computed values or adding
            logic when accessing data.

@<property_name>.setter: Allows you to define a "setter" method for a property, giving you control over how
            an attribute is modified.

🚀 Additional Example: Using Property for Read-Only Attribute
'''
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# Usage
c = Circle(10)
print(c.area)  # 314.0 (Area is calculated)

# In this case, area is read-only (computed dynamically) and doesn’t have 
# a setter because we don’t want users to set the area directly.