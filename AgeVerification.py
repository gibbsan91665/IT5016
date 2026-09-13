# Boolean Comparisons
# Challenge 2.2
from datetime import date

year_of_birth = input("\nPlease enter your year of birth: ")
name = input("Please enter your name: ")
current_year = (date.today().year)
print("\nThe result of your application is",
str((current_year - int(year_of_birth) >= 21)
and name != "Suzanne May"
and name != "Wiremu Rangi"), ".")
