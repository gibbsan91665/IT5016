# BooleanAnd.py
# 

is_alive = True
time_remaining = False

# Test case assertion 1: result should be False
print("The game in progress status is....\n")
print(is_alive and time_remaining, "\n")

print("Giving more time to play...\n")
time_remaining = True

# Test case assertion 2: result should be True
print("The game in progress status is now....\n")
print(is_alive and time_remaining, "\n")
