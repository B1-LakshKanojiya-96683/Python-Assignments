# A pangram is a sentence that contains all the letters of the English alphabet at least once.
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.


alphabet=("abcdefghijklmnopqrstuvwxyz")
sentence= input("Enter your sentence to check for panagram ")
sentence=sentence.lower()
list1=list(sentence)
list2=list(alphabet)

for x in alphabet:
    if x in list1:
        list2.remove(x)
    elif list2==[]:
        break
    else: 
        continue

if list2==[]:
        print("This sentence is a panagram ")
        
else:
     print("This sentence is not a panagram")