# Python Cheat Sheet

# Data Types
# 1. Integer
x = 5
print(type(x))  # Output: <class 'int'>

# 2. Float
y = 3.14
print(type(y))  # Output: <class 'float'>

# 3. String
name = "Alice"
print(type(name))  # Output: <class 'str'>

# 4. List
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>

# 5. Dictionary
person = {"name": "Bob", "age": 30}
print(type(person))  # Output: <class 'dict'>

# Control Structures
# 1. If Statement
if x > 0:
    print("Positive")

# 2. For Loop
for fruit in fruits:
    print(fruit)

# 3. While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Libraries
# 1. Importing a library
import math

# 2. Using a library function
print(math.sqrt(16))  # Output: 4.0

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# File Handling
# 1. Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# 2. Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)