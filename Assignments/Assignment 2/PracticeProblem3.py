#program to create 4 functions of calculator and store them in a list

def addition(num1, num2):
    return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply (num1,num2):
    return num1*num2

def divide (num1,num2):
    return num1/num2

Function_List = [addition, subtract, multiply, divide]

for x in Function_List:
    print(f"{x(10,10)}")