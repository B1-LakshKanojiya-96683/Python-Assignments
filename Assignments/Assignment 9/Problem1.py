# 1. Create a tuple to store information of a person. Reverse the tuple (in a new tuple) and print it.


tuple1=()
n= int(input("Enter the number of information pieces that you would like to store about yourself    " ))
list1=[]

for x in range(0,n):
    string=input("Enter info    ")
    list1.append(str(string))

tuple1=tuple(list1)

for x in range (0,n):
    list1[x]=str(tuple1[n-1-x])

tuple2=tuple(list1)
print(f"The information in reverse is this :   {tuple2}")
