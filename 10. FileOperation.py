#  In Python, reading and writing files is typically done using the built-in open() function,
#  which provides a file object for interacting with a file on your disk.

#🔹 open() Function Syntax : open(file, mode='r', encoding=None)

# 1. file - Path to the file (absolute or relative).
# 2. mode - in which the file is opened 
# 3. encoding - used to decode or encode the file (e.g., "utf-8"). Used only in text mode.
#             Default Value for encoding - is None, which makes Python choose the 
#             platform-dependent default encoding:
#                 a. On Windows, this is usually "cp1252" or another ANSI code page.
#                 b. On Linux/macOS, it's usually "utf-8".

# To check your system's default encoding:
import locale
print(locale.getpreferredencoding(False)) # Output : cp1252


'''
| Mode| Description                                           |
| ----| ------------------------------------------------------|
| 'r' | Read (default mode). File must exist.                 |
| 'w' | Write. Creates a new file or overrites existing file. |
| 'a' | Append. Creates file if not exists; appends data.     |
| 'x' | Exclusive creation. Fails if file exists.             |
| 'b' | Binary mode. e.g., 'rb', 'wb'                         |
| 't' | Text mode (default). e.g rt, but it is equivalen to r |
| '+' | Allows both Read and Write. e.g., 'r+', 'w+'          |

Must be combined with 'r', 'w', or 'a'.
✅ Common combinations:
Mode	Description
'r+'	Read and write. File must exist.
'w+'	Write and read. Overwrites or creates file.
'a+'	Append and read. Creates file if it doesn't exist.
'''
# Reading from a File
with open('Python\FileOperation.txt', 'r', encoding='utf-8') as file:
    content = file.read() # Read entire file
    # print(content)

# Other Read Methods
# file.readline()   # Read one line
# file.readlines()  # Read all lines into a list

# Writing to a File
# used r'filePath' - Python interprets \t as a tab character because \ is an escape character in strings.
# with open(r'Python\\test.txt', 'w', encoding='utf-8') as file:
with open(r'Python\test.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!")

# Appending to a File - Append creates file if not exists; appends data.
with open('Python\example.txt', 'a', encoding='utf-8') as file:
     file.write("\nAppended line.")    #\n - appends on new line
    
# Checking if File Exists (Before Reading or Writing)
import os

filePath = 'Python\example.txt'

if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        print(file.read())

# Closing the File (Without with)
# Use of Try:finally ie. Exception Handling in Python
file = open(filePath, "r", encoding="utf-8")
try:
    data = file.read()
finally:
    file.close()
  
# Read file line by line till the end of the file
# Efficient for large files since it doesn't load the entire file into memory.  
filePath = 'Python\example.txt'

with open(filePath, 'r', encoding='utf-8') as file:
    line_count = 0      # line Counter
    for line in file:
        line_count += 1     # counter + 1
        print(line.strip())  # .strip() removes leading/trailing whitespace like \n
        
print(line_count)

# | Method           | Memory Efficient | Fast for Large Files | Simple Syntax  | Notes                |
# | -----------------| ---------------- | -------------------- | -------------- | -------------------- |
# | for line in file | ✅ Yes           | ✅ Yes              | ✅ Yes         | ✅ Best choice      |
# | file.readline()  | ✅ Yes           | ⚠️ Slightly slower  | ❌ Manual loop | For fine control     |
# | file.readlines() | ❌ No            | ❌ No               | ✅ Simple      | Only for small files |

# file.readlines()
# Reads entire file into memory as a list of lines.
# Bad for large files: high memory usage, potential MemoryError.
# Slightly slower due to list creation and memory overhead.