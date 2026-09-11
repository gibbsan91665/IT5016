# ListIterate.py
#

sample_list = [1, 4, 5, 2, 9, 12]
for item in sample_list:
    print("An item in the sample list is ", item)

# If you need both the index and the item, use the enumerate function:
for index, item in enumerate(sample_list):
    print("The element index is ", index, " and the value is ", item)

# If you need only the index, use range and len:
for index in range(len(sample_list)):
    print("The element index is ", index)

# The list object supports the iterator protocol. To explicitly
# create an iterator, use the built-in iter function:
i = iter(sample_list)
item = i.__next__() # fetch first value
print("An item in the sample list is ", item)
item = i.__next__() # fetch second value
print("An item in the sample list is ", item)

# Python provides various shortcuts for common list operations. For example,
# if a list contains numbers, the built-in sum function gives you the sum:
list_sum = sum(sample_list)
print("The sum of the items in the list is.... ", list_sum)
subtotal = 23
total = sum(sample_list, subtotal)
print("The sum of the items in the list and another number is.... ", total)
average = float(sum(sample_list)) / len(sample_list)
print("The average of the items in the list is.... ", average)

# If a list contains strings, you can combine the string into
# a single long string using the join string method:
haka_list = ["Taringa", "whakarongo!", "Kia", "rite!", "Kia", "rite!"]
joined_list = " ".join(haka_list)
print("The joined list is....", joined_list)
