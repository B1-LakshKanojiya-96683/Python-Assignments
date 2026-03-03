#4. Write a Python program that calculates the sum of the squares of all odd numbers
#in a list of integers using map() and filter()
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


is_odd= lambda odd: odd%2==1
odd_list = list(filter(is_odd,numbers))

square = lambda sq : sq**2
squared=list(map(square,odd_list))
print(squared)
