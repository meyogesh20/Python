'''
 1. Syntax Errors - What it is ?
    - Occur when Python code is not syntactically correct.
    - Detected before the program runs (during parsing).

Example - 

if True
    print("Missing colon")    # Output --> SyntaxError: expected ':'
    
'''
# 🔍 Fix syntax errors before execution — they’re like grammar mistakes in code.

#----------------------------------------------------------------------------------------------
'''
2. Exceptions - What it is ?
    - Occur during execution when something goes wrong (runtime errors).
    - Examples: ZeroDivisionError, FileNotFoundError, TypeError, etc.

Example - 

print(10 / 0)    ZeroDivisionError: division by zero

''' # 📌 Exceptions can be caught and handled to prevent your program from crashing.

#----------------------------------------------------------------------------------------------
# 3. Handling Exceptions - Use try...except block:
# It is possible to write programs that handle selected exceptions.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result is", result)
finally:
    print("Execution complete.")

'''
try: code that may raise an exception.
except: handle specific exception.
else: runs if no exceptions occur.
finally: always runs, for cleanup.

The try statement works as follows.
1. First, the try clause (the statement(s) between the try and except keywords) is executed.
2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.
3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, 
   if its type matches the exception named after the except keyword, the except clause is executed, and
   then execution continues after the try/except block.
4. If an exception occurs which does not match the exception named in the except clause, it is passed on
   to outer try statements; if no handler is found, it is an unhandled exception and execution stops with
   an error message.

 📌 try...except Matching Logic:
Python matches except clauses top-down. It checks each except in the order they appear, and matches the
first compatible exception type. Once a match is found, other except blocks are ignored for that exception.
🧠 Rule of Thumb
Always order except blocks from most specific to most general.

* A try statement may have more than one except clause, to specify handlers for different exceptions. 
At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding
try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions
as a parenthesized tuple

# for example:
try :
    num = int(input("Enter a number: "))
    result = 10 / num
except (RuntimeError, TypeError, NameError):
     pass
'''
#----------------------------------------------------------------------------------------------
# 🚫 4. Raising Exceptions
# 🔹 Use raise to manually trigger an exception:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

# Useful for enforcing conditions or input validation.

#----------------------------------------------------------------------------------------------
# 5. Exception Chaining
# 🔹 Use raise ... from ... to link exceptions:

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse input") from e

''' Helps trace(find) original cause (root exception).
ValueError: invalid literal for int() with base 10: 'abc'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "d:\Data Science 2024\VS_Code\Python\tempCodeRunnerFile.py", line 4, in <module>
    raise RuntimeError("Failed to parse input") from e
RuntimeError: Failed to parse input '''

#----------------------------------------------------------------------------------------------
# 6. Raising and Handling Multiple Unrelated Exceptions
# 🔹 Example with multiple except clauses:
# Python matches exceptions in the order you write them.

try:
    x = int("abc")  # ValueError
    y = 1 / 0       # ZeroDivisionError
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Divide by zero")
    
#----------------------------------------------------------------------------------------------
# 7. Defining Clean-up Actions
# 🔹 Use finally block:

try:
    f = open("myfile.txt", "r")
    # Read something
except FileNotFoundError:
    print("File not found")
finally:
    f.close()  # Always executed
    
#----------------------------------------------------------------------------------------------
# 8. Enriching Exceptions with Notes (Python 3.11+)
# 🔹 Use .add_note() to add more context:

try:
    raise ValueError("Something went wrong")
except ValueError as e:
    e.add_note("Occurred during input validation")      # will add note to the exception object
    raise   # this actually raises error from object e

#----------------------------------------------------------------------------------------------
# 9. A classic behavior of exception class hierarchy and how except clauses are matched in Python.

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    print(f"\nRaising: {cls.__name__}")
    e = cls()  # Create instance of the exception class

    print(f"  Actual type of e: {type(e).__name__}")

    # Manual isinstance checks
    print(f"  isinstance(e, B): {isinstance(e, B)}")
    print(f"  isinstance(e, C): {isinstance(e, C)}")
    print(f"  isinstance(e, D): {isinstance(e, D)}")

    # Simulate what try-except does
    try:
        raise e
    except B:
        print("  -> Handled by except B")
    except C:
        print("  -> Handled by except C")
    except D:
        print("  -> Handled by except D")

'''--------------------------------------------------------------------------------------------
# Output Explaination
Raising: B
  Actual type of e: B
  isinstance(e, B): True
  isinstance(e, C): False
  isinstance(e, D): False
  -> Handled by except B

Raising: C
  Actual type of e: C
  isinstance(e, B): True   # C inherits from B
  isinstance(e, C): True
  isinstance(e, D): False
  -> Handled by except B   # First match, even though C is more specific

Raising: D
  Actual type of e: D
  isinstance(e, B): True   # D → C → B
  isinstance(e, C): True
  isinstance(e, D): True
  -> Handled by except B   # Because B is first
'''
#----------------------------------------------------------------------------------------------
''' 10. 📘 Python Exception Hierarchy
The class hierarchy for built-in exceptions is:
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
           
🔍 Key Concepts:
BaseException: The root of all exceptions. You should rarely catch this directly.
Exception: The base class for most errors. You should catch this when you want to handle general exceptions.
Subclasses group exceptions into categories:
    ArithmeticError: Numeric errors like division by zero.
    OSError: Filesystem and OS-related errors.
    LookupError: Errors accessing a collection by key or index.
'''
# Example Usage:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", e)
except ArithmeticError as e:
    print("Caught an ArithmeticError:", e)  # This also would catch it
except Exception as e:
    print("Caught a general exception:", e)

#----------------------------------------------------------------------------------------------