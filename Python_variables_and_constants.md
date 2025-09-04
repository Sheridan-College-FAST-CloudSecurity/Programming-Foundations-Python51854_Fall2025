In Python, a variable is a symbolic name that stores data or a value in the computer's memory. Variables allow programmers to label data so it can be used and manipulated throughout a program. Python variables are dynamically typed, which means you don’t need to declare their type explicitly; the interpreter assigns it automatically based on the value. 

Creating Variables
You create a variable by simply assigning a value using the = operator:
name = "Alice"       # String variable
age = 25             # Integer variable
height = 5.6         # Float variable
is_student = True    # Boolean variable
**
Rules for Naming Variables**
Names can contain letters, digits, and underscores (_).
Must start with a letter or underscore.
Cannot be a Python keyword (like if, for, class).
Case-sensitive (age ≠ Age).

Multiple Assignments

Python allows assigning multiple variables in one line:
x, y, z = 10, 20, 30

Dynamic Typing
Python allows you to change the type of a variable:
value = 10         # Integer
value = "Ten"      # Now a string

Types of python variables:
1. Numeric Types
Python supports three main numeric types:
int → whole numbers
float → decimal numbers
complex → numbers with real and imaginary parts
x = 10         # int
y = 3.14       # float
z = 2 + 5j     # complex

2. String Type (str)
A sequence of Unicode characters.
name = "Alice"

3. Boolean Type (bool)
Represents True or False.
is_active = True

constant in Python is just a variable whose value is not meant to change during the program.
⚠️ Unlike C or Java, Python does not have true built-in constants — it relies on naming conventions.

By convention, constants are written in all uppercase letters with underscores:
PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299_792_458

Rules for Constants in Python
Naming convention
Use UPPERCASE letters.
Words are separated by underscores (_).
Example: MAX_VALUE, DATABASE_URL.

Placement
Usually defined at the top of the file.
Sometimes grouped in a separate constants.py module.
No Reassignment (by practice, not enforcement)
PI = 3.14
PI = 3.14159   # ❌ Bad practice (changes constant)
Should represent fixed values
Numbers, strings, or configuration values that should not change.
Avoid hardcoding values in code
Instead of:
area = 3.14 * r * r
Use:
PI = 3.14
area = PI * r * r
