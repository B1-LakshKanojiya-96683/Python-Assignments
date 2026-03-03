#7) Write a function filter_long_words() that takes a list of
#  words and an integer len and returns the list of words that 
# are longer than len.

list_len=0
list1=[]

list_len=int(input("Enter the no of words that you want to have in your list"))

print("Now enter the words of the list one by one")

for x in range (list_len):
    print("Enter word")
    list1.append(input())

length_to_be_checked= int (input("Enter the number of characters based on which you want to filter words out"))

def filter_long_words(list2,check_len):
    new_list=[]
    for x in list2:
        if len(x)>check_len:
            new_list.append(x)
        else:
            continue

    return new_list

result = filter_long_words(list1,length_to_be_checked)
print(f"{result}")