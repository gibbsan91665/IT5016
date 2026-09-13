# If Statements
# Challenge 1.4 (Optional)

choice = (input("If you would like to find the surface area of a shape enter Surface, "
"if you would like to find the volume of a shape type Volume?\n\n"))
if choice.lower() == "surface":
  side_a = int(input("Enter the length of cuboid\n\n"))
  side_b = int(input("Enter the width of cuboid\n\n"))
  side_c = int(input("Enter the height of cuboid\n\n"))
  print("\nThe surface area of the cuboid is ",
        side_a * side_b * 2
        + side_b * side_c * 2
        + side_a * side_c * 2
        ,"\n\n")

if choice.lower() == "volume":
  side_a = int(input("Enter the length of cuboid\n\n"))
  side_b = int(input("Enter the width of cuboid\n\n"))
  side_c = int(input("Enter the height of cuboid\n\n"))
  print("\nThe volume area of the cuboid is ", side_a * side_b * side_c,"\n\n")

if choice.lower() != "volume" and choice.lower() != "surface":
  print("\nYou can only enter surface of volume""\n\n")

# Testing
'''
print("My assertions are:"
"\nchoice = surface, side_a = 6, side_b = 5, side_c = 4 output = 148"
"\nchoice = volume, side_a = 6, side_b = 5, side_c = 4 output = 120"
"\nchoice = shape output = You can only enter surface or volume")
'''
