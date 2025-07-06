# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:06:57 2024

@author: cedrick joseph
"""

# Python Crash Course (Comprehensive)

# ============================================
# 1. Variables and Data Types
# ============================================
# Variables are used to store data. In Python, you don't need to declare the type of a variable.
# Python automatically infers the type based on the value assigned.

# Example:
x = 10          # x is an integer (int)
y = 20.5        # y is a floating-point number (float)
name = "Alice"  # name is a string (str)
is_student = True  # is_student is a boolean (bool)

# Python has several built-in data types:
# - int: Integer numbers (e.g., 10, -5)
# - float: Decimal numbers (e.g., 3.14, -0.001)
# - str: Text data (e.g., "Hello", 'Python')
# - bool: Boolean values (True or False)
# - list: Ordered, mutable collection of items (e.g., [1, 2, 3])
# - tuple: Ordered, immutable collection of items (e.g., (1, 2, 3))
# - set: Unordered collection of unique items (e.g., {1, 2, 3})
# - dict: Key-value pairs (e.g., {"name": "Alice", "age": 25})

# ============================================
# 2. Typecasting
# ============================================
# Typecasting is the process of converting one data type to another.
# This is useful when you need to perform operations on data of different types.

# Example:
x = 10
y = float(x)    # Convert int to float (10 -> 10.0)
z = str(x)      # Convert int to string (10 -> "10")
p
# Common typecasting functions:
# - int(): Converts to integer
# - float(): Converts to float
# - str(): Converts to string
# - bool(): Converts to boolean

# ============================================
# 3. Inputs
# ============================================
# The `input()` function is used to take input from the user.
# By default, `input()` returns a string, so you may need to typecast it.

# Example:
name = input("Enter your name: ")  # Takes a string input
age = int(input("Enter your age: "))  # Takes an integer input

# Note: If the user enters a non-integer value for `age`, it will raise an error.
# You can handle this using exception handling (explained later).

# ============================================
# 4. Booleans
# ============================================
# Booleans represent one of two values: `True` or `False`.
# They are often used in conditional statements and loops.

# Example:
is_raining = True
is_sunny = False

# Boolean expressions evaluate to `True` or `False`.
print(10 > 5)   # Output: True (10 is greater than 5)
print(10 == 5)  # Output: False (10 is not equal to 5)

# ============================================
# 5. F-Strings (Formatted String Literals)
# ============================================
# F-strings allow you to embed expressions inside string literals using curly braces `{}`.
# They make string formatting more readable and concise.

# Example:
name = "Alice"
age = 25
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Output: Hello, Alice! You are 25 years old.

# You can also perform operations inside f-strings:
print(f"In 5 years, you will be {age + 5} years old.")  # Output: In 5 years, you will be 30 years old.

# ============================================
# 6. Logical Operators
# ============================================
# Logical operators are used to combine conditional statements.
# - `and`: True if both conditions are True
# - `or`: True if at least one condition is True
# - `not`: Inverts the boolean value

# Example:
age = 25
is_student = True

if age > 18 and is_student:
    print("You are an adult student.")  # Output: You are an adult student.

if age < 18 or is_student:
    print("You are either under 18 or a student.")  # Output: You are either under 18 or a student.

if not is_student:
    print("You are not a student.")
else:
    print("You are a student.")  # Output: You are a student.

# ============================================
# 7. Loops
# ============================================
# Loops are used to repeat a block of code.

# For Loop:
# Used to iterate over a sequence (e.g., list, tuple, string, range).
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)  # Output: 0 1 2 3 4

# While Loop:
# Used to repeat a block of code as long as a condition is True.
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1

# ============================================
# 8. Functions
# ============================================
# Functions are reusable blocks of code defined using the `def` keyword.
# They can take inputs (arguments) and return outputs.

# Example of a simple function:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Example of a function with a return value:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# ============================================
# 9. Lambda Functions
# ============================================
# Lambda functions are small, anonymous functions defined with the `lambda` keyword.
# They are useful for short, one-time operations.

# Syntax: lambda arguments: expression

# Example:
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda functions are often used with functions like `map`, `filter`, and `reduce`.

# Example with `map`:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example with `filter`:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# ============================================
# 10. Conditional Statements
# ============================================
# Conditional statements are used to make decisions in your code.
# Python uses `if`, `elif`, and `else` for conditional logic.

# Example:
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

# ============================================
# 11. Lists and List Operations
# ============================================
# Lists are ordered, mutable collections of items.

# Example:
my_list = [1, 2, 3, 4, 5, 10, 6]

# Accessing elements:
print(my_list[0])  # Output: 1 (first element)
print(my_list[-1])  # Output: 5 (last element)

# Adding elements:
my_list.append(6)  # Adds 6 to the end of the list
my_list.insert(-1, 10)  # Inserts 0 at the beginning of the list

# Removing elements:
my_list.remove(3)  # Removes the first occurrence of 3
popped_element = my_list.pop()  # Removes and returns the last element

# ============================================
# 12. Dictionaries
# ============================================
# Dictionaries store key-value pairs.

# Example:
my_dict = {"name": "Alice", "age": 25}

# Accessing values:
print(my_dict["name"])  # Output: Alice

# Adding or updating values:
my_dict["age"] = 26  # Updates the age
my_dict["city"] = "New York"  # Adds a new key-value pair

# Removing values:
del my_dict["city"]  # Removes the key "city"

# ============================================
# 13. Sets
# ============================================
# Sets are unordered collections of unique elements.

# Example:
my_set = {1, 2, 3, 4, 5}

# Adding elements:
my_set.add(6)

# Removing elements:
my_set.remove(3)

# Set operations:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)  # {3}

# ============================================
# 14. File Handling
# ============================================
# Python allows you to read from and write to files.

# Writing to a file:
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!

# ============================================
# 15. Exception Handling
# ============================================
# Exception handling is used to handle errors gracefully.

# Example:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

# ============================================
# 16. Other Functions in Python
# ============================================

# The map() function is used to apply a specific function to every item in an iterable
# (like a list, tuple, etc.) and return a map object (which is an iterator).

#The join() method is used to concatenate (combine) a list of strings into a single
# string, with a specified separator between the elements.

# The enumerate() function adds a counter to an iterable and returns it as an enumerate
# object (which can be converted to a list of tuples).

# The reversed() function returns a reverse iterator for an iterable.

# The all() function returns True if all elements in an iterable are True (or if the iterable is empty).

# min(): Returns the smallest item in an iterable.

# max(): Returns the largest item in an iterable.

# The len() function returns the number of items in an iterable or the length of a string.

# The range() function generates a sequence of numbers, commonly used in loops.

# The type() function returns the type of object.

# The any() function returns True if at least one element in an iterable is True.

# ============================================
# End of Python Crash Course (Comprehensive)