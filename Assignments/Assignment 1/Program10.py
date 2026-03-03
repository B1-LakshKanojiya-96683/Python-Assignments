#The marks obtained by a student in 3 different subjects are input by the user. Your
   # program should calculate the average of subjects and display the grade. The student
  #  gets a grade as per the following rules:
 #   Average Grade
# 90-100 A
  #  80-89 B
  #  70-79 C
  #  60-69 D
  #   0-59 F


marks1=int(input("Enter the Marks of first subject"))
marks2=int (input("Enter the Marks of 2nd subject"))
marks3=int(input("Enter the marks of 3rd subject"))
Grade = "to be calculated"
i=0
average = (marks1+marks2+marks3)/3
if marks1>=0 and marks1<=100 and marks2>=0 and marks2<=100 and marks3>=0 and marks3<=100:
    i=0
else:
    i=1
if average >=90 and average <=100:
    Grade = "A"
elif average >=80 and average <90:
    Grade ="B"
elif average >=70 and average <80:
    Grade = "C"
elif average>=60 and average <70:
    Grade ="D"
elif average >= 0 and average <60:
    Grade ="F"

if i!=1:
    print(f"Your grade is   {Grade}")
