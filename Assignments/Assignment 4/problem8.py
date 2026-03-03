#8. Write a Python Program to find the repeated item of a
# tuple(Take a value from user which you want to find)

tuple1= []
n=int(input("Enter the number of elements you want to have in your tuple"))
for x in range (n):
    tuple1.append(int(input("Enter number")))           #taking input from the user 

tuple1=tuple(tuple1)                #converting list recieved from the user into tuple

value=int(input("enter the value that you want to find in the list "))

val_count=tuple1.count(value)

if val_count>1:
    print ("This number exists in the list")
elif val_count==1:
    print("This value exists only once in the list")
else:
    print("this value does not exist in the list")