''''
2. Write a Python program to replace dictionary values(V,VI)and with their average.
Input:-
student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]

Expected Output:
[{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5},
{'subject': 'math', 'id': 3, 'V+VI': 80.5} ] 
'''

student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]

avg=lambda x: (x["V"]+ x["VI"] )/2 
result=list(map(avg, student_details))
print(result)
y=0
for x in student_details:
    del x["V"]
    del x['VI']
    x["V+VI"] = result[y]
    y=y+1

print(f"The new modified values of V and VI in the dictionary is as follows {student_details}")
