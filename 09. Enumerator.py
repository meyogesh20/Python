# 🔹 What is enumerate()?
# The enumerate() function lets you loop over a sequence (like a list or string)
# and get both the index and the value at the same time.
''' 
    Basic Syntax - enumerate(iterable, start=0)
    iterable: iterable must be a sequence, an iterator, 
              or some other object which supports iteration.
    start: optional, the number you want indexing to start from (default is 0).
'''
# Example
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output :
# 0 apple
# 1 banana
# 2 cherry

''' If you want to indexting from 1 '''
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output :
# 1 apple
# 2 banana
# 3 cherry

''' Common Use Case: When you need both the index and the value while looping'''
for i, char in enumerate("hello"):
    print(f"Character at index {i} is {char}")

''' enumerate() with string '''  
text = "abc"
for i, char in enumerate(text):
    print(f"Index {i}: {char}")
 
# Output :   
# Index 0: a
# Index 1: b
# Index 2: c

''' enumerate() with tuple ''' 
colors = ('red', 'green', 'blue')
for i, color in enumerate(colors):
    print(f"{i}: {color}")

''' enumerate() with Set (Unordered, so index order is not predictable) 
    ⚠️ Since sets are unordered, the output order can vary. '''
     
items = {'pen', 'book', 'ruler'}
for i, item in enumerate(items):
    print(i, item)
    
    
''' enumerate() with Dictionary (using keys) ''' 
my_dict = {'a': 1, 'b': 2}
for i, key in enumerate(my_dict):
    print(f"Index {i}, Key: {key}, Value: {my_dict[key]}")


''' Using enumerate() in List Comprehensions 
You can use enumerate() to build new lists while keeping track of indexes.''' 

# Example: Prefix each item with its index
names = ['alice', 'bob', 'carol']
result = [f"{i}: {name}" for i, name in enumerate(names)]
print(result)

# Output: ['0: alice', '1: bob', '2: carol']
 
#---------------build a custom version of enumerate()------------------------
# ✅ Why Use collections.abc.Iterable?
# It's the official way to check if something supports iteration.
# Safer than relying on hasattr(obj, '__iter__').

from collections.abc import Iterable

def my_enumerate(iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise TypeError("The argument 'iterable' must be an iterable object")
    
    index = start
    for item in iterable:
        yield (index, item)
        index += 1

print(list(my_enumerate(['a', 'b', 'c'])))  # ✅ Works fine
print(list(my_enumerate(123)))              # ❌ Raises TypeError: 
#                                           The argument 'iterable' must be an iterable object


