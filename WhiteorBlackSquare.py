# If Statements
# Challenge 1.1

row_letter = 0
choice_row = (input("Enter the row letter of the square\n\n"))
if choice_row.lower() == ("a" or "c" or "e" or "g"):
row_letter = 1
choice_col = int(input("Enter the column number of the square\n\n"))
coordinate_reference = choice_col + row_letter
if coordinate_reference % 2 == 0:
print("\nThe square is black""\n\n")
else:
print("\nThe square is white""\n\n")

# Testing
'''
print("My assertions are:"
"\nchoice_row = a, choice_col = 1, output = black"
"\nchoice_row = f, choice_col = 3, output = white")
'''
