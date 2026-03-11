"""
5. Input a string from user and display unique characters in it. Hint: list(str) convert string to list of chars.
Input: programming
Output: ['p', 'r', 'o', 'g', 'a', 'm', 'i', 'n']   """


string = "programming"
list_output=[]

for x in string:
    if x not in list_output:
        list_output.append(x)

print(list_output)