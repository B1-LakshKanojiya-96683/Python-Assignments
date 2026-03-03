#6. Write a Python program that filters out all strings that have more 
# than 5 characters from a list of strings using the filter() function.
#Input : words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
#Output : ['Yellow','Purple','Orange']

words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']

character_filter= lambda string : len(string) > 5

result = list(filter(character_filter,words))

print (f"{result}")
