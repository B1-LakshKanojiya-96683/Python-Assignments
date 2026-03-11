# 2. Write a Python program to find repeated items in a tuple.


tuple1=[]
n=int(input("Enter the numeber of elements of the tuple   "))
for x in range(0,n):
    tuple1.append(input("Enter value"))
checking_list=[]
confirmation=0
tuple1=tuple(tuple1)

for x in tuple1:
    if tuple1.count(x)>1:
        confirmation+=1
        if x not in checking_list: 
            print(f"The element {x} is present {tuple1.count(x)} times and is getting repeated")
            checking_list.append(x)

    elif confirmation==0:
        print("no item is repeated")


