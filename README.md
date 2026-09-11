# IT5016 Assessment 3: Programming Principles and Concepts
# A collection of handy list functions

# list.append(elem) - Adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
# list_1.extend(list_2) - Appends all of list_2 elements to the end of list_1.
# list.insert(index, elem) - Inserts the element at the given index, shifting elements to the right.
# list.index(elem) - Searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError - see below).
# list.remove(elem) - Searches for the first instance of the given element and removes it (throws ValueError if not present).
# list.sort() - Sorts the list in place (does not return it).
# list.reverse() - Reverses the list in place (does not return it).
# list.pop(index) - Removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
# if value in L: - A boolean check to find out if a value exists in the list L.

# Use i, j, and k as variables in for statements. This is a coding convention recognised by experienced developers.
# Use the for statement to iterate a list.
# Use the "for element in list:" syntax to search for an item in a list. This approach avoids the error that might occur if the item being searched for does not exist in the list.
# Use list_name.append(item) to add an item to the end of the list.
# Use the pop() method to remove an item at the given index. This method returns the item being removed. It is a useful method since it simulates the removal of something from a collection.
# Use the pop() method to remove and return the last item if the index is not provided. This helps us implement lists as stacks (first in, last out data structure).
# Use list.count(item) to return the number of elements that are equal to the item.
# Use the built-in sort() and reverse() methods to do sorting.
