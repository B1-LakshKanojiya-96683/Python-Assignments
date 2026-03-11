"""
6. In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower().
   ```python
   text = Python is a high-level, general-purpose programming language. Its design 
philosophy emphasizes code readability with the use of significant indentation. Python is
 dynamically typed and garbage-collected. It supports multiple programming paradigms,
    including structured, object-oriented and functional programming.

"""

text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."
text=text.lower()
dict1={}
list_check=[]
print("The information about letter frequency is given below  :")
for x in text:
    if x != ' ' and x not in list_check:
        dict1[x]=text.count(x)
        list_check.append(x)
        print(f"{x}  :  {dict1[x]} ")
    else:
        continue
