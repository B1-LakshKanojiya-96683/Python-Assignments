#6. Find all of the numbers from 1-1000 that are divisible by 7. Solve Using list Comprehension.

list1=[x for x in range (1,1000) if x%7==0]

print(f"The numbers from 1 to 1000 divisible by 7 are    {list1}")