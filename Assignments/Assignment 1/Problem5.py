#5] Write a Python function to find the maximum of three numbers.

num1=int (input("enter the first number"))
num2=int(input("enter the 2nd number"))
num3 = int (input("enter the 3rd number"))
res=0
y=0
if num1>num2 and num1>num3:
    res = num1
elif num2>num1 and num2> num3:
    res = num2
elif num3>num1 and num3>num2:
    res = num3
elif num3==num2 and num2>num1:
    res = num2
    y=y+1
elif num3==num1 and num1>num2:
    res = num1
    y=y+1
elif num2 == num1 and num1>num3:
    res = num2 
    y=y+1
else:
    print("all numbers ar equal")
    y=2

if y==0:
    print(f"the largest number is {res}")
elif y==1:
    print(f"there are two numbers which are equal and larger than the third = {res}" )