"""11.  Write a Python program that filters out all palindromes from a list 
of strings using the filter() function.
words = ['level', 'radar', 'hello', 'world', 'madam']"""

words = ['level', 'radar', 'hello', 'world', 'madam']
def palindrome(string):

    rev_string= string[::]
    if rev_string==string[::-1]:
        return True
    else:
        False

result = list(filter(palindrome,words))

print(f"{result}")
