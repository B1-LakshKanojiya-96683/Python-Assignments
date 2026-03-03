#5. Write a Python program that adds two lists element-wise using the map() function.
 #   input :   list1 = [1, 2, 3, 4, 5]
  #            list2 = [5, 4, 3, 2, 1]
   # Expected Output  : [6, 6, 6, 6, 6]

list1 = [1, 2, 3, 4, 5]                     #creating the list 1
list2=[5,4,3,2,1]           #craeted list 2

add=lambda list_a, list_b: list_a+list_b        # using lambda function to claculate list sum

final_result =list(map(add,list1,list2))    # storing the list addition

print(f"{final_result}")