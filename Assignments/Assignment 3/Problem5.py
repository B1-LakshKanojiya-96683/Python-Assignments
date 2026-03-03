#5) Define a function overlapping() that takes two lists and returns 
# True if they have at least one member in common, False 
# otherwise.

list1=[]
list2=[]
a=0
p=0
q=0
count =0


def overlapping():

    a=int(input("Enter the number of elements you want to have in the first list"))
    print("Now start entering the elements of the first list")
    for x in range (0,a):
        new_ele=input()
        list1.append(new_ele)
    
    b=int (input("Enter the no. of elements of the second list"))
    print("Start entering the elements of the second list now")
    for x in range (0,b):
        new_ele=input()
        list2.append(new_ele)

    if a>b:
        p=a
        q=b
    else:
        p=b
        q=a

    for x in range (0,p):
        for y in range (0,q):
            if str(list1[x]) == str(list2[y]):
             global count
             count = count +1
             break
    
    if count >0:
        return True
    else:
        return False


result = overlapping()
print(f"the result of the overalapping function is {result}")