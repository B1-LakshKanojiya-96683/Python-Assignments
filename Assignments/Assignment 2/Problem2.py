#Q2: Define four functions (add, subtract, multiply, 
#divide), store them in a list, iterate over the list, and call each function with 
# values (10, 20). Print the results.

def add(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def subtract(num1, num2): 
    return num1 - num2

def divide(num1, num2):   
    return num1 / num2

# Create list of 'tools'
operations = [add, subtract, multiply, divide]

# Now iterate over them
for func in operations:
    result = func(10, 20)
    print(result)

