#1. Write a Python program that finds the longest word in a list of strings. Use map()
#  to calculate the length of each word, and filter() to get the word with the maximum length.
#words = ["python", "functional", "programming", "is", "powerful"]

words = ["python", "functional", "programming", "is", "powerful"]
str_len=0

def transformation_function(recieved):
    str_len= len(recieved)
    return str_len 

list_of_length= list(map(transformation_function,words))

print(f"{list_of_length}")

largest_word=max(list_of_length)
print(f"{largest_word}")

def selection_function(string2):
    if len(string2) == largest_word:
        return True
    else:
        return False
    
max_length_item=list(filter(selection_function,words))
print(f"the max length word is {max_length_item}")