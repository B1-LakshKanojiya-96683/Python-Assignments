#7) Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
 # Dictionary's value should be stored in list. Your dictionary should be like:
 # {'EVEN':[8,10,64], 'ODD':[1,5,9]} 

even=[]
odd=[]
y=int(input("Please enter how many numbers you would like to input?"))

for x in range (y):
    input_number=int(input("Enter number"))
    
    if input_number %2==0:
        even.append(input_number)
    else:
        odd.append(input_number)

final_dict= {"EVEN": even , "ODD": odd}
print(final_dict)