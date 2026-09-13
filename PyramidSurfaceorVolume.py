# If Statements
# Challenge 1.6 (Optional)

choice = (input("If you would like to find the surface area of a shape enter Surface, "
"if you would like to find the volume of a shape type Volume?\n"))

if choice.lower() == "surface":
  base = int(input("Enter the base of the pyramid\n"))
  height = int(input("Enter the height of the pyramid\n"))
  print("\nThe surface area of the pryamid is ", base/2 * height * 4 + base ** 2,"\n")

if choice.lower() == "volume":
  base = int(input("Enter the base of the pyramid\n"))
  height = int(input("Enter the height of the pyramid\n"))
  print("\nThe volume area of the pyramid is ", base ** 2 * height / 3,"\n")

if choice.lower() != ("volume" or "surface"):
  print("\nYou can only enter surface or volume""\n")

# Testing
'''
print("My assertions are:"
"choice = surface, base = 5, height = 4, output = 65"
"choice = volume, base = 5, height = 4, output = 33.33"
"choice = shape output = You can only enter surface or volume")
'''
