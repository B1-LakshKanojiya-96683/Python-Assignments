# Write a method in python to display the elements of list thrice if it
#is a number and display the element terminated with ‘#’ if it is not a number.
#Hint-: Use InBuilt Function isdigit()
#Refer below as a input:-
#mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]


def process_list(lst):
    for item in lst:
        if item.isdigit():
            print(item * 3)
        else:
            print(item + "#")

mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']
process_list(mylist)
