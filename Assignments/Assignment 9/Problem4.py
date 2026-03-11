"""
4. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
   - Input: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
   - Output: [30.5, 34.25, 27.0, 23.25]  """


Input_tuple=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
sum=0
avg_list=[]

for x in range(len(Input_tuple)):
    for y in Input_tuple:
        sum = sum + y[x]
    average=sum/len(y)
    avg_list.append(average)
    sum=0

print (f"The average is  {avg_list}")
