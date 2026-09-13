# If Statements
# Challenge 1.5 (Optional)

import math
choice = (input("If you would like to find the surface area of a shape enter Surface, "
"if you would like to find the volume of a shape type Volume?\n\n"))

if choice.lower() == "surface":
  length = int(input("Enter the length of cylinder\n\n"))
  radius = int(input("Enter the radius of circle\n\n"))
  print("\nThe surface area of the cylinder is ",
        2 * math.pi * radius * length
        + 2 * math.pi * radius ** 2
        ,"\n\n")

if choice.lower() == "volume":
  length = int(input("Enter the length of cylinder\n\n"))
  radius = int(input("Enter the radius of circle\n\n"))
  print("\nThe volume area of the cuboid is ", math.pi * radius ** 2 * length,"\n\n")

if choice.lower() != "volume" and choice.lower() != "surface":
  print("\nYou can only enter surface of volume""\n\n")

# Testing
'''
print("My assertions are:"
"\nchoice = surface, length = 6, radius = 3, output = 169.65"
"\nchoice = volume, length = 6, radius = 3, output = 169.65"
"\nchoice = shape output = You can only enter surface or volume")
'''
