# Python Lists
# Challenge 1.2

list_2 = [1,19,4,8]
list_3 = ["land of ", "the ", "the long white cloud"]
temp_list = [list_2, list_3]
list_to_print = []

for item in temp_list:
  if len(item) > len(list_to_print):
    list_to_print = item

print("\nThe longest list contains {0} elements."
  .format(len(list_to_print)))
print("\nThe list is {0}"
  .format(list_to_print))

# Test Case Assertions:
# Assertion 1: "The longest list contains 4 elements."
