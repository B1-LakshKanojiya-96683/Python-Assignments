#1.Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



list_of_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

swap = lambda x: (x[1], x[0])

swapped = list(map(swap, list_of_tuples))
swapped.sort()

final_list = list(map(swap, swapped))

print(final_list)
