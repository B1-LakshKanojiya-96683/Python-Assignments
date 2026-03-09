"""3. Write a program that display following output:
 SHIFT
 HIFTS
 IFTSH
 FTSHI
 TSHIF
 SHIFT"""

#first approach to solving this problem
string=input("Enter the string")
list1=list(string)
print(string)
bstr=list1
for x in range (len(string)):
    store=bstr[0]
    bstr.pop(0)
    bstr.append(store)
    result="".join(bstr)
    print(result)

#second approach to solving this problem
string=input("Enter the string")
for i in range (len(string)):
   print( string[i:]+string[:i])
print(string)
