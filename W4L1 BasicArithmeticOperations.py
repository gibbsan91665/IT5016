# basic_arithmetic_oerations
# week4 - Lab1

def add(a, b):
  return a + b

def multiply(x, y):
  return x * y

def add_and_multiply(a, b, c):
  sum_result = add(a, b) # Calling the add function
  product_result = multiply(sum_result, c) # Calling the multiply function
  return product_result

result = add_and_multiply(2, 3, 4)
print(result) # Output: 20
