"""

1) Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
A. Find out how many students are in the list
B. Change Lisa’s favourite colour
C. Remove 'Jenny' and her favourite colour
D. Sort and print students and their favourite colours alphabetically by name


"""


people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

student_count=len(people)

print(f"There are   {student_count}    students in the dictionary")


people['Lisa']="brown"
del people['Jenny']

print("The name and favourie colour of the remaining students is")
for x in sorted(people):
    print(f"name = {x}   favourite colour = {people[x]}")