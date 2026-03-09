"""4. Calculate the sum and average of the digits
 present in a string Str1="Python83737@#8496"
expected Output : sum = 55 avg = 6.111""
"""

digit =['1','2','3','4','5','6','7','8','9','0']
Str1=input("Enter the string")
print()
sum = 0
count=0
for x in Str1:
    if x in digit:
        count=count+1
        sum =  sum + int(x)
print(f"The sum of digits is   {sum}")
average= sum/count
print(f"The average is {average}")