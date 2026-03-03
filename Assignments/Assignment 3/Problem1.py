#1) Using for loop, write and run a Python 
# program to find factorial from 0 to 10.


factorial = 1
for x in range (1,11):
    factorial = factorial*x
    
print(f"The factorial is {factorial}")