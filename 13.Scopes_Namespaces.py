'''
A Word About Names and Objects — a core idea in Python that's important to understand, 
especially when dealing with mutable objects like lists and dictionaries.
 
Basic Idea: Names Point to Objects
In Python: A name (like a variable) is just a label or a reference.
An object is a thing in memory — like a number, list, or dictionary.
'''
# When you do something like this:
a = [1, 2, 3]
b = a

# You're not copying the list. You're saying: ➡️ "b points to the same list object that 'a' does."
# This is called "aliasing" — two names referring to the same object.

# If you change the list using either name, both see the change:

b.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
'''
🔹Immutable vs Mutable
Immutable objects: (like numbers, strings, tuples) can't be changed.
If you try to modify them, Python just creates a new object.

Mutable objects: (like lists, dictionaries) can be changed. 
If two variables point to the same object, and one changes it, both see the change.

🔹 Why This Matters
This behavior allows Python to:
Be efficient (no unnecessary copying).
Act like it's using pointers (like in C/C++) — behind the scenes.
Pass objects to functions cheaply, by just passing a reference.
'''
# When you pass an object to a function, changes inside the function affect the original object.

def add_item(mylist):
    mylist.append(100)

nums = [1, 2, 3]
add_item(nums)
print(nums)  # Output: [1, 2, 3, 100]

#✅ The list nums changed inside the function — because both mylist and nums referred to the same object.

'''
Python scopes and namespaces : 
🔁 Namespace - A namespace is a mapping of names to objects (like variables or functions).
Examples: built-in namespace, global namespace (per module), local namespace (per function call).

Namespaces are isolated: same name can exist in multiple namespaces without conflict 
(e.g., module1.func vs module2.func).
Think of namespaces as "dictionaries of names."

📦 Scope - A scope is a region of code where a namespace is directly accessible.
When you use a variable name, Python looks for it in this order (called LEGB Rule):

Local - inside the current function
Enclosing - inside enclosing functions (if using nested functions)
Global - at the top level of the module
Built-in - predefined names like len, abs, etc.

📘 Key Behavior
global - declares that a variable inside a function should refer to the module-level (global) variable.
nonlocal - allows a variable in a nested function to refer to a variable in its enclosing (non-global) function.
Assignments always create or update names in the innermost (local) scope, unless overridden by global or nonlocal.

📌 Key Concepts:
local: creates a new variable in the current function.
nonlocal: modifies a variable from the nearest enclosing scope (but not global).
global: modifies or creates a variable in the module-level (global) scope.

'''
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam         # global : create new variable spam at global scope (outside scope_test())
        spam = "global spam"

    spam = "test spam"      # after do_nonlocal(), spam == "nonlocal spam"
    do_local()
    print("After local assignment:", spam)      # Output : After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)   # Output : After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam)     # Output : After global assignment: nonlocal spam

scope_test()                                    # scope_test() finishes, all local stack discarded

print("In global scope:", spam)                 # Output : In global scope: global spam

# above line refers to the global variable created by do_global() function during scope_test() function exeuction

# One more example :

x = "global"

def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "inner"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
print("global:", x)

# Output - 
# inner: inner
# outer: inner
# global: global


