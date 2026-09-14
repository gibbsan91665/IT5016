# Slicing Lists
# Challenge 1.3

list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42, 1, 2, 19, 108]
length = len(list_1)
if length % 4 == 0:
  quarter = (int(length/4))
  three_quarters = quarter * 3
  print(list_1[three_quarters:length])

# Test Case Assertion
# Assertion 1: output = [2, 19, 108]
