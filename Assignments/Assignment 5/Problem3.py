"""             

3. Write a program in Python to remove repetitive items from a list.
Hint Given num = [2,3,4,5,2,6,3,2]
Expected output Result: [2, 3, 4, 5, 6] New list    

"""


num = [2,3,4,5,2,6,3,2]

remover=lambda x: num.remove(x)



for y in num:
    if num.count(y)>1:
        remover(y)
    else:
        continue
num.sort()
print(f"{num}")