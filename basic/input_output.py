# 1. Simple string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Taking numeric input (requires type conversion)
# The input is initially a string, so we convert it to an integer using int()
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# 3. Taking multiple inputs in one line
# Use split() to break the input string into a list of strings, then convert
x, y = map(int, input("Enter two numbers separated by a space: ").split())
print(f"The sum of {x} and {y} is {x + y}.")