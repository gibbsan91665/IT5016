# BooleanNot.py
# 

is_full_attendance = True
is_mark_below_pass = False

# Test case assertion 1: result should be True
print("The student's success status is....\n")
print(is_full_attendance and not is_mark_below_pass, "\n")

print("Student failed their exam...\n")
is_mark_below_pass = True

# Test case assertion 2: result should be False
print("The student's success status is now....\n")
print(is_full_attendance and not is_mark_below_pass, "\n")
