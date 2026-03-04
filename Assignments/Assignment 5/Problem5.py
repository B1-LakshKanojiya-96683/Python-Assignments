#  5. Create a list of tuples where each tuple contains a number and its square for numbers
#  from 0 to 9. Solve using list comprehension.

list1=[(x,x**2) for x in range(0,10)]

print(f"The required listof tuples of the numbers from 0 to 9 along with their squares is     {list1}")