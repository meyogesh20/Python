# A lambda expression is a small, anonymous function defined using the lambda keyword.
# Basic Syntax - lambda arguments: expression

# Traditional function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

# Single Argumnet
f = lambda x: x + 10
print(f(5))  # Output: 15

# Multiple Arguments
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Conditional Login in Lambda
max_val = lambda a, b: a if a > b else b
print(max_val(8, 5))  # Output: 8

# Use with map() function
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]

# Use with filter() function
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# Use in sorted() function for custom key 
data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [(1, 'apple'), (3, 'banana'), (2, 'cherry')]

# with functools e.g reduce() function
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # 24

# Lambda with default Values
f = lambda x=5, y=10: x + y
print(f())       # 15
print(f(2, 3))   # 5

# Lambda in dictionary (Dynamic Dispatch)
operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y
}
print(operations['add'](3, 5))  # 8

# Use of *args and **kwargs in lambda
sum_all = lambda *args: sum(args)

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100

# Multiply All Arguments
from functools import reduce
multiply_all = lambda *args: reduce(lambda x, y: x * y, args)

print(multiply_all(2, 3, 4))  # Output: 24

# You can also combine *args and **kwargs in lambda expressions:
func = lambda *args, **kwargs: (args, kwargs)

print(func(1, 2, a=3, b=4))
# Output: ((1, 2), {'a': 3, 'b': 4})
