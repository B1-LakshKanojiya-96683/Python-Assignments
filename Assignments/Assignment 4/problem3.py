#3. Write a Python program to convert a given list of integers and a tuple of integers into a list  of strings.
#Use Python map.

numbers_list = [1, 2, 3, 4]
numbers_tuple = (5, 6, 7, 8)

# Using map to convert integers to strings
list_of_strings = list(map(str, numbers_list))
tuple_converted_to_strings = list(map(str, numbers_tuple))

# Displaying the results
print("List of strings:", list_of_strings)
print("Tuple converted to list of strings:", tuple_converted_to_strings)