# TuplePractice.py
#

bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
 ("Tama", 6000),
  ("Suzanne", 21025, "45 Green Lane"),
   ("Anihera", -75))

print("The number of bank accounts is ", len(bank_accounts))

# showing names and balances
for i in bank_accounts:
  print("\nThe name is ", i[0], " and the balance is $", i[1])

# showing only names with addresses
for i in bank_accounts:
  if len(i)>2:
    print("\nThe name is ", i[0], " and the address is ", i[2])

# show customers with less than $100
low_balance = 100
for i in bank_accounts:
  if i[1] < low_balance:
    print("\nA customer with less than ${0} is {1}".format(
      low_balance, i[0]))

# showing only customers with no phone number or no addresses
for i in bank_accounts:
  if len(i) <= 2:
    print("\nA customer with either no number or address is ", i[0])

# showing the highest and lowest balances
# get a list of the balances
balances_list = []
for i in bank_accounts:
  balances_list.append(i[1])
print("\nThe highest balance is ${0}.".format(max(balances_list)))
print("\nThe lowest balance is ${0}.".format(min(balances_list)))
print("\nThe sum of all balances is ${0}.".format(sum(balances_list)))

# showing all details for all customers
print("\nShowing details for all customers...")
for i in bank_accounts:
  print("\n")
  for customer_detail in i:
    print(customer_detail, end=" ")

# showing only customers with more than $5k or less than $0
print("\n\nShowing details for our rich and poor customers...", end="")
for i in bank_accounts:
  if 0 > i[1] or i[1] > 5000:
    print("\n")
    for customer_detail in i:
      print(customer_detail, end=" ")
