# accessing_a_global_variable.py
# week4 - Lab1
count = 0
def increment():
  global count # Declare 'count' as global
  count += 1
  print(f"Count inside function: {count}")

# Call the function
increment()
increment()

# Access the global variable
print(f"Count outside Function: {count}")
