#6) Find and display the largest number of 
# a list without using built-in function 
# max(). Your program should ask the user to input values in list
#  from keyboard.


list1=[]
print("Please enter the no of elements you want to have in the string" )
n=int(input())
print("Now start entering the numbers in the list")
for x in range (0,n):
    new_element=int(input())
    list1.append(new_element)

list1.sort()
print(f"The largest number of this list is {list1[n-1]}")