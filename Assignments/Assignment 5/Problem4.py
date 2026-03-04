"""

4. Python program to create a list of tuples from given list having number and its cube in each tuple.
I/P-[1,2,5,6]  Output-[(1, 1), (2, 8), (5, 125), (6, 216)]

"""


list1=[1,2,5,6]

list_of_tuples=[]

num_and_square=lambda x: (x,x**3)

list2=list(map(num_and_square,list1))

print(f"The required output is   {list2}")