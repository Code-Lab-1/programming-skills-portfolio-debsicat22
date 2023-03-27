
# Importing the math module to access the value of pi
import math

# Accepting the radius of the circle as input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculating the area of the circle using the formula pi * r^2
area = math.pi * (radius ** 2)

# Printing the area of the circle
print("The area of the circle is: " + str(area))
