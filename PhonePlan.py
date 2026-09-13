# If Statements
# Challenge 1.3

from decimal import Decimal

minutes = int(input("Enter the number of minutes used this month\n\n"))
texts = int(input("Enter the number of texts sent this month\n\n"))
base_rate = 1500
additional_minutes_cost = 25
additional_texts_cost = 15
allowed_minutes = 50
allowed_texts = 50
cost_of_extra_minutes = 0
cost_of_extra_texts = 0
call_centre_fee = 44
tax = 0
subtotal = 0
print("Your base fee is: $",base_rate/100,"\n")

if minutes > allowed_minutes:
  cost_of_extra_minutes = (minutes - allowed_minutes) * additional_minutes_cost
  print("Your addtional minutes fee is: ", cost_of_extra_minutes/100 ,"\n")

if texts > allowed_texts:
  cost_of_extra_texts = (texts - allowed_texts) * additional_texts_cost
  print("Your additional texts fee is: ", cost_of_extra_texts/100,"\n")
print("Your 111 call centre fee is: $",call_centre_fee/100,"\n")
subtotal = base_rate + cost_of_extra_minutes + cost_of_extra_texts + call_centre_fee
tax = subtotal * 0.05

print("Taxes: $", round(tax/100,2),"\n")
print("Subtotal: $", subtotal/100,"\n")
print("Total Charges: $",round((subtotal + tax)/100,2),"\n")

# Testing
'''
print("My assertions are:"
"minutes = 40, texts = 55, output = additional_texts_cost = 0.75, tax = 0.81, Total Charges:
$17.00"
"minutes = 55, texts = 40, output = additional_minutes_cost = 1.25, tax = 0.83, Total Charges:
$17.52"
"minutes = 40, texts = 40, output = tax = 0.77, Total Charges: $16.21"
"minutes = 55, texts = 55, output = additional_minutes_cost = 1.25, additional_texts_cost =
0.75, tax = 0.87, Total Charges: $18.31")
'''
