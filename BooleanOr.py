# BooleanOr.py
# @ author: A. N. Other
# date: September 2016

is_fuel_in_tank = True
is_driver_licensed = False
is_driver_insured = True

print("This program works out whether you can have a car, or a driver....\n")

# Test case assertion 1: result should be True
print("Program output is ", is_fuel_in_tank or is_driver_licensed and is_driver_insured, "\n")

print("Removing all the fuel...\n")
is_fuel_in_tank = False

# Test case assertion 2: result should be False
print("Program output is now ", is_fuel_in_tank or is_driver_licensed and is_driver_insured, "\n")
