#4) In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower(). Do not use Counter collection.

#text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""


text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."
string1=""
text2=text.lower()
print("   Letter  -   Occurence")
check_against=[]

for x in text2:
    if x.isalpha():
        if x in check_against:
            continue
        else:
            print(f"   {x}    -     {text2.count(x)}")
            check_against.append(x)