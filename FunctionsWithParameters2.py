# Function3.py
# Functions with Parameters 2

first_number = 6
second_number = 4

def show_difference(number_1, number_2):
  print("The first number is {0}.\n"
    "The second number is {1}.\n"
    "The difference between them is {2}!!!\n"
    .format(number_1, number_2, number_1 - number_2))

print("Welcome to my difference calculator...\n\n")

# invoking the function
show_difference(first_number, second_number)

# Test Case Assertions:
# Assertion 1:
# print("Test case assertion: if first number is 13 and second number is 2 "
# "then the difference should be 11!!")
# show_difference(13, 2)
