# Program to demonstrate stripping of whitespaces

# Defining a string variable with whitespaces at the beginning and end
name = "\t\n   Leonardo DiCaprio   \n\t"

# Printing the original string with whitespaces
print("Original String: " + name)

# Printing the string after stripping the left side whitespaces using lstrip()
print("Left Stripped String: " + name.lstrip())

# Printing the string after stripping the right side whitespaces using rstrip()
print("Right Stripped String: " + name.rstrip())

# Printing the string after stripping both the left and right side whitespaces using strip()
print("Completely Stripped String: " + name.strip())
