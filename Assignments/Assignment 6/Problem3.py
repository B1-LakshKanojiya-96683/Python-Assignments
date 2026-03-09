"""
3) Define a function subtract() that takes two lists and returns 
difference (i.e. excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20].

"""

subtract = lambda x: [x for x in first_list if x not in second_list ]
first_list=[10, 20, 30, 40]
second_list= [30, 40, 50, 60]

result=subtract(first_list)

print(result)