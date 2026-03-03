#2. Write a Python program to double all numbers in a given list of integers. Use Python map,lambda function.
#list1 = [1,2,3,4,5,6,7,8,9]

list1 = [1,2,3,4,5,6,7,8,9]

double=lambda twice: twice*2       #recieves the parameter in the variable twice and returns the double of 'twice' variable

list2=list(map(double,list1))


print(f"{list2}")