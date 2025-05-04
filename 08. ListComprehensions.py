# 🔷 What Are List Comprehensions?
# List comprehensions are a concise way to create new lists by applying
# an expression to each item in an iterable (like a list, tuple, or range),
# optionally filtering elements (ie. if-condition).
# General Syntax - [expression for item in iterable if condition].
'''
A list comprehension consists of brackets containing an expression followed by a for clause,
then zero or more for or if clauses. The result will be a new list resulting from 
evaluating the expression in the context of the for and if clauses which follow it.
'''
#--------------------------------------------------------------------------------
# This is how below program works.
# Takes x from range(5)
# Applies x**2 to each x
# Collects results into a list
#--------------------------------------------------------------------------------
''' 1. Simple Example '''
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

''' 2. With a condition (filtering ie. if condition) '''
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # Output: [0, 2, 4, 6, 8]

''' 3. Use a conditional expression instead of an if filter: '''
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)   # Output: ['even', 'odd', 'even', 'odd', 'even']

''' 4. Nested Loops : Flatten a matrix (2D list) '''
# Note: Loops are read left to right, same as nested for statements.
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)   # Output: [1, 2, 3, 4, 5, 6]

''' 5. Cartesian Product (like itertools.product) '''
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs) # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

#--------------------------------------------------------------------------------

# Real World Examples
''' 1. Extract digits from a string '''
digits = [int(ch) for ch in "a1b2c3" if ch.isdigit()]
print(digits)   # Output: [1, 2, 3]

''' 2. Convert strings to uppercase '''
names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
print(upper_names)     # Output: ['ALICE', 'BOB', 'CAROL']

''' 3. Remove Falsy Values '''
# 0, False, None and empty sequences are interpreted as False
values = ["", "hello", None, "world", 0]    
filtered = [val for val in values if val]
print(filtered)     # Output: ['hello', 'world']

''' 4. Get square of even number only '''
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)     # Output: [0, 4, 16, 36, 64]

''' 5. Read a file and strip newlines '''
#lines = [line.strip() for line in open("file.txt")]
#print(lines)

''' 6. Dictionary to list of key-value strings '''
d = {'a': 1, 'b': 2}
kv_strings = [f"{k}={v}" for k, v in d.items()]
print(kv_strings)  # Output: ['a=1', 'b=2']

''' 7. Create a list of 2-tuples like (number, square) '''
# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)] - raises SyntaxError: did you forget parentheses around the comprehension target?

list_tuple = [(x, x**2) for x in range(6)]
print(list_tuple)   # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
 
#--------------------------------------------------------------------------------
# ⚠️ When Not to Use List Comprehensions
# Avoid when:
#   1. The logic is too complex (use a regular loop for clarity).
#   2. You’re doing side effects (like print(), file I/O) — better use a for loop.
#--------------------------------------------------------------------------------

''' Dictionary, Set and Generator Expression also supports comprehension '''

# Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With Condition
even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}

# From 2 lists using zip() function
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}

#--------------------------------------------------------------------------------
# Set Comprehension - Removes duplicates and keeps unique elements.
unique_squares = {x**2 for x in [1, 2, 2, 3]}
# Output: {1, 4, 9}

# With Condition
even = {x for x in range(10) if x % 2 == 0}

#--------------------------------------------------------------------------------
# Generator Expression - Returns a generator (lazy evaluation, saves memory)

squares_gen = (x**2 for x in range(10))      #Use it with next() or in a for loop:

# for val in squares_gen:
#     print(val)

# using next()
print(next(squares_gen))    # Output: 0
print(next(squares_gen))    # Output: 1
print(next(squares_gen))    # Output: 4
print(next(squares_gen))    # Output: 9
print(next(squares_gen))    # Output: 16
print(next(squares_gen))    # Output: 25 # continues...
print(next(squares_gen))    # ❌ Raises StopIteration - if tried to get item after printing last item
