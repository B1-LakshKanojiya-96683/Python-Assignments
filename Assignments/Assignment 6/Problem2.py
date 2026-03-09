"""2) Write a program to sum all the values of a dictionary.
Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
Expected output
Result: 500
"""


dict1 = {'key1': 200, 'key2': 300}

sum=0
for x in dict1:
    sum = sum + dict1[x]

print(f"The sum of all the values of the dictiionary is   {sum}")