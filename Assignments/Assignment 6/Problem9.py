"""
9) Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hanga salami I'm a lasagna hog.", 
"Was it a rat I saw?", 
"Step on no pets", 
"Sit on a potato pan, Otis", 
"Lisa Bonet ate no basil", 
"Satan, oscillate my metallic sonatas", 
"I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.

"""


string = input("Enter the string to check for palindrome")
list1 = []

for x in string.lower():
    if x.isalpha():
        list1.append(x)

clean_string = "".join(list1)
reverse_string = clean_string[::-1]

if clean_string == reverse_string:
    print("This phrase is a palindrome")
else:
    print("This phrase is not a palindrome")