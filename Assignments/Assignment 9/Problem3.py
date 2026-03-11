"""
3. Write a Python program to remove an empty tuple(s) from a list of tuples.
   - Input: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
   - Output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

"""


list_of_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new_list = []

for item in list_of_tuples:
   
    if item:
        new_list.append(item)

list_of_tuples = new_list
print(list_of_tuples)