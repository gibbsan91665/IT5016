# Python Lists
# Challenge 1.1

list_1 = [23,66,23,12]
list_2 = [1,19,4,8]
list_sum = (sum(list_1) + sum(list_2))

user_input = input("Type Sum or Average.\n\n")

if user_input.lower() == "sum":
  print("\nThe sum of the items in the list is.... ",list_sum,"\n")

if user_input.lower() == "average":
  print("\nThe average of the items in the list is.... ",list_sum/4,"\n")

if user_input.lower() != "sum" and user_input.lower() != "average":
  print("\nYou can only enter sum or average""\n")

# Testing
'''
print("My assertions are:"
"\nuser_input = sum, output = 156"
"\nuser_input = average, output = 19.5")
'''
