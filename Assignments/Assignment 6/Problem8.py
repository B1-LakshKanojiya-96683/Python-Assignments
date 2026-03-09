"""

8) Write a function translate() that will translate a text into "rövarspråket"
  (Swedish for "robber's language"). That is, double every consonant and place an
  occurrence of "o" in between. For example, translate("this is fun") should return
  the string "tothohisos isos fofunon".
  
  """


vowels=['a','e','i','o','u']
list1=[]
string="this is fun"

def translate():
    for x in string:
        if x not in vowels and x != " ":
            string2=x+"o"+x
            list1.append(string2) 
        else:
            list1.append(x)

    result="".join(list1)

    print(result)
    print(list1)

translate()